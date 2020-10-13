from sqlite_utils import Database
from djangobench.main import discover_benchmarks, DEFAULT_BENCHMARK_DIR

db = Database("django.db")

commits = [commit['sha'] for commit in db["commits"].rows_where(select="sha")]
benchmarks = discover_benchmarks(DEFAULT_BENCHMARK_DIR)

