import os
from datetime import datetime, timedelta
import datetime as dt
import sys
import platform

def main():
    name = os.getenv("PIPELINE_NAME","demo")
    now = datetime.now(dt.timezone.utc).isoformat()
    print(f"{now} pipeline={name} Python ={sys.version.split()[0]} os = {platform.platform()}")
    rows = [{"id": i, "amount": i*10} for i in range(1, 10)]
    total = sum(r["amount"] for r in rows)
    print(f"Processed {len(rows)} rows, total = {total}")



if __name__ == "__main__":
    main()