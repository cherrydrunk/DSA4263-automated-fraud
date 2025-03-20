import re
import pandas as pd
import os

current_directory = os.getcwd()
base_dir_phase1 = 'data/web_bot_detection_dataset/phase1/data/web_logs'
base_dir_phase2 = 'data/web_bot_detection_dataset/phase2/data/web_logs'

def web_log_df(directory):
    humans_web_log_dir = directory + '/humans'
    bots_web_log_dir = directory + '/bots'
    log_pattern = re.compile(
        r'- - \[(?P<datetime>[^]]+)\] "(?P<method>\S+) (?P<url>\S+) (?P<protocol>\S+)" (?P<status>\d+) (?P<byte_size>\d+) "(?P<referrer>[^"]*)" (?P<Session_ID>\S+) "(?P<user_agent>[^"]+)"'
    )
    parsed_logs = []
    for i in [humans_web_log_dir,bots_web_log_dir]:
        if i == humans_web_log_dir:
            label = "humans" 
        else:
            label = "bots"
        for log in os.listdir(i):
            with open(i + '/' + log, 'r') as file:
                log_entries = file.readlines()

            for log in log_entries:
                match = log_pattern.match(log)
                if match:
                    log_data = match.groupdict()
                    log_data["category"] = label 
                    parsed_logs.append(log_data)

    df = pd.DataFrame(parsed_logs)
    df['datetime'] = pd.to_datetime(df['datetime'], format="%d/%b/%Y:%H:%M:%S %z").dt.tz_localize(None)
    return df

web_log_phase1 = web_log_df(base_dir_phase1)
web_log_phase2 = web_log_df(base_dir_phase2)


web_log_phase1.to_csv('data/interim/web_log_phase1.csv', index=False)
web_log_phase2.to_csv('data/interim/web_log_phase2.csv', index=False)