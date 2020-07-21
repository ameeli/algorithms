// Implement a stopwatch object.

function Stopwatch() {
  let duration, startTime = 0;

  this.start = function() {
    if (!startTime) {
      startTime = Date.now();
    } else {
      throw new Error('Timer already started');
    }
  };

  this.stop = function() {
    if (startTime) {
      duration = Date.now() - startTime;
      startTime = 0;
    } else {
      throw new Error('Timer not started');
    }
  };

  this.reset = function() {
    duration = 0;
  }

  Object.defineProperty(this, 'duration', {
    get: function() {
      return duration / 1000;
    }
  });
}
