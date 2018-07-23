"""
You are in charge of a display advertising program. Your ads are displayed on websites all over the internet. You have some CSV input data that counts how many times you showed an ad on each individual domain. Every line consists of a count and a domain name. It looks like this:

counts = [ "900,google.com",
     "60,mail.yahoo.com",
     "10,mobile.sports.yahoo.com",
     "40,sports.yahoo.com",
     "300,yahoo.com",
     "10,stackoverflow.com",
     "2,en.wikipedia.org",
     "1,es.wikipedia.org" ]
     
Write a function that takes this input as a parameter and returns a data structure containing the number of hits that were recorded on each domain AND each domain under it. For example, an impression on "sports.yahoo.com" counts for "sports.yahoo.com", "yahoo.com", and "com". (Subdomains are added to the left of their parent domain. So "sports" and "sports.yahoo" are not valid domains.)     

Expected output (in any order):
1320    com
 900    google.com
 410    yahoo.com
  60    mail.yahoo.com
  10    mobile.sports.yahoo.com
  50    sports.yahoo.com
  10    stackoverflow.com
   3    org
   3    wikipedia.org
   2    en.wikipedia.org
   1    es.wikipedia.org

"""

def count_hits_per_domain(data):
    domain_counts = {}
    for domain in data:
        domain = domain.split(',')
        domain_counts[domain[1]] = int(domain[0])
    
    hits_per_domain = {}
    for key in domain_counts:
        # split domain string into words array
        words_in_domain = key.split('.')
        words_in_domain_index = 2
        subdomain = words_in_domain[-1]
        hits_per_domain[subdomain] = hits_per_domain.get(subdomain, 0) + domain_counts[key]
        
        while words_in_domain_index <= len(words_in_domain):
            # add subdomain key to hits_per_domain
            subdomain = words_in_domain[-words_in_domain_index] + '.' + subdomain
            hits_per_domain[subdomain] = hits_per_domain.get(subdomain, 0) + domain_counts[key]
            words_in_domain_index += 1
    
    output = ''
    for domain in hits_per_domain:
        output = output + str(hits_per_domain[domain]) + '\t' + domain + '\n'
        
    return output
                                

counts = [ "900,google.com",
     "60,mail.yahoo.com",
     "10,mobile.sports.yahoo.com",
     "40,sports.yahoo.com",
     "300,yahoo.com",
     "10,stackoverflow.com",
     "2,en.wikipedia.org",
     "1,es.wikipedia.org" ]
     
print count_hits_per_domain(counts)
