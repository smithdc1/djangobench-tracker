from sqlite_utils import Database
from djangobench.main import discover_benchmarks, DEFAULT_BENCHMARK_DIR, run_benchmarks
import os


def run_bench():
    db = Database("django.db")

    commits = [commit['sha'] for commit in db["commits"].rows_where(select="sha", order_by="committer_date desc")]
    benchmarks = list(discover_benchmarks(DEFAULT_BENCHMARK_DIR))
    tested_commits = {commit['experiment_commit'] for commit in db["bench"].rows_where(select="experiment_commit")}

    for idx, commit in enumerate(commits):
        if commit not in tested_commits:
            experiment = commit
            control = commits[idx + 1]
            break

    print(control, experiment)
    os.chdir('django')
    run_benchmarks(control, experiment, DEFAULT_BENCHMARK_DIR, benchmarks, 5, vcs='git', record_dir="../json_output")


if __name__ == '__main__':
    run_bench()
