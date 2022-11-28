""" job v1 mod """
import threading
from shared_code.step import Step

def process(data: dict, content: dict, method: str, option:dict = None):
    """ process content """
    if method == 'run':
        out = data_job = data
        option = option if option else {}
        if 'steps' in data_job:
            step = int(option['step'])-1 if 'step' in option else 0
            step_len = len(data_job['steps'])
            limit = int(option['limit']) \
                if 'limit' in option and \
                    int(option['limit']) < (step_len - step) \
                else (step_len - step)
            print(f"Step {step} Limit {limit} step_len {step_len}")

            if 0 <= step < step_len:
                step_input = content

                for idx in range(step, step+limit):
                    print(f"Index {idx+1} out of {step+limit}")
                    data_step = data_job['steps'][idx]
                    if 'async' in data_step and data_step['async']:
                        # running step async
                        print("running async")
                        thread = threading.Thread(
                            target=Step.run,
                            args=(data_step, step_input))
                        thread.start()
                    else:
                        step_input = out = Step.run(data_step, step_input)
        return out
    return content
