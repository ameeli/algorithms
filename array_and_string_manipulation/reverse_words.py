def reverse_words(message):
    """Decode the message by reversing the words"""
    reverse_message(message, 0, len(message) - 1)
    word_start_index = 0
    
    for i in range(len(message) + 1):
        if i == len(message) or message[i] == ' ':
            reverse_message(message, word_start_index, i - 1)
            word_start_index = i + 1

def reverse_message(message, start_index, end_index):
    """Reverse characters in message in place"""
    while start_index < end_index:
        message[start_index], message[end_index] = message[end_index], message[start_index]
        start_index += 1
        end_index -= 1