""" job v1 mod """
import threading
from shared_code.step import Step

def process(data: dict, content: dict, method: str, params:dict):
    """ process content """
    if method == 'run':
        out = data_job = data
        params = params if params else {}
        if 'steps' in data_job:
            step = int(params['step'])-1 if 'step' in params else 0
            step_len = len(data_job['steps'])
            limit = int(params['limit']) \
                if 'limit' in params and \
                    int(params['limit']) < (step_len - step) \
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
                            args=(data_step, step_input, params))
                        thread.start()
                    else:
                        step_input = out = Step.run(data_step, step_input, params)
        return out
    return content
