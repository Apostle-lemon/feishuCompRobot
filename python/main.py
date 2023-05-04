import internal.store.store_data_to_sql as store
import schedule
import time

def Job():
    store.main()

# 每周三的 11:30 执行一次 job
schedule.every().wednesday.at("11:30").do(Job)
# 每周六的 11:30 执行一次 job
schedule.every().saturday.at("11:30").do(Job)

while True:
    schedule.run_pending()
    time.sleep(30)

