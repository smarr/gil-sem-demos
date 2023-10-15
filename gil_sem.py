from threading import Thread


class ResultThread(Thread):
    """
    A thread that stores the result of a function call
    or an assertion error if it occurred.

    Thread should not prevent program from exiting,
    and is thus made a daemon thread.
    """

    def __init__(self, fn, args):
        super().__init__()
        self.fn = fn
        self.args = args
        self.result = None
        self.assertion = None

        self.daemon = True

    def run(self):
        try:
            self.result = self.fn(*self.args)
        except AssertionError as e:
            print(e)
            self.assertion = e

    def result_or_assertion(self):
        """
        Return the result of the function call
        or the assertion error if it occurred.
        """
        if self.assertion:
            return self.assertion
        return self.result


def start_and_await(threads):
    """
    Start threads and wait for them to finish
    and return their results.

    If any thread raises an AssertionError,
    it is returned as result.
    """
    for t in threads:
        t.start()

    results = []
    no_failure = True

    while threads and no_failure:
        remaining_threads = []
        for t in threads:
            t.join(0.1)
            if t.is_alive():
                remaining_threads.append(t)
            else:
                if t.assertion:
                    no_failure = False
                results.append(t)
        threads = remaining_threads
    return results


def report_error_or_success(results):
    """
    Print the errors of the threads, or no thread failed, print "Success".
    """
    for r in results:
        if r.assertion:
            raise r.assertion
    print("Success")
