"""Collect real course evidence inside Skills Network Theia; never invent results."""

import argparse
import datetime
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidence"


def run_and_save(name, command, directory=ROOT):
    """Save the exact command, timestamp, actual output, and exit status."""
    completed = subprocess.run(
        command, cwd=directory, text=True, stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT, check=False,
    )
    transcript = (
        f"Captured: {datetime.datetime.now(datetime.timezone.utc).isoformat()}\n"
        f"$ {' '.join(command)}\n{completed.stdout}"
        f"\nExit status: {completed.returncode}\n"
    )
    path = EVIDENCE / f"{name}.txt"
    path.write_text(transcript, encoding="utf-8")
    print(transcript)
    print(f"Saved {path.relative_to(ROOT)}")
    return completed.returncode


def save_code_snippets():
    """Copy the exact source file required by each code submission question."""
    sources = {
        "2a_emotion_detection": "evidence/stages/task2/emotion_detection.py",
        "3a_output_formatting": "evidence/stages/task3/emotion_detection.py",
        "5a_unit_testing": "test_emotion_detection.py",
        "6a_server": "server.py",
        "7a_error_handling_function": "EmotionDetection/emotion_detection.py",
        "7b_error_handling_server": "server.py",
        "8a_server_modified": "server.py",
    }
    for name, source in sources.items():
        (EVIDENCE / f"{name}.txt").write_text(
            (ROOT / source).read_text(encoding="utf-8"), encoding="utf-8"
        )


def main():
    """Collect local evidence or opt in to live Watson calls inside Theia."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", action="store_true",
                        help="Also run real Watson tests; requires Theia Lab")
    args = parser.parse_args()
    EVIDENCE.mkdir(exist_ok=True)
    save_code_snippets()
    statuses = [
        run_and_save("offline_tests", [sys.executable, "-m", "unittest",
                                      "tests.test_offline", "-v"]),
        run_and_save("8b_static_code_analysis", [sys.executable, "-m",
                                               "pylint", "server.py"]),
    ]
    if args.live:
        statuses.extend([
            run_and_save("2b_application_creation", [sys.executable, "-c",
                         'from emotion_detection import emotion_detector; '
                         'print(emotion_detector("I love this new technology."))'],
                         ROOT / "evidence/stages/task2"),
            run_and_save("3b_formatted_output_test", [sys.executable, "-c",
                         'from emotion_detection import emotion_detector; '
                         'result = emotion_detector("I am so happy I am doing this"); '
                         'print(result); assert result["dominant_emotion"] == "joy"'],
                         ROOT / "evidence/stages/task3"),
            run_and_save("4b_packaging_test", [sys.executable, "-c",
                         'from EmotionDetection.emotion_detection import emotion_detector; '
                         'result = emotion_detector("I hate working long hours"); '
                         'print(result); assert result["dominant_emotion"] == "anger"']),
            run_and_save("5b_unit_testing_result", [sys.executable, "-m",
                                                  "unittest", "test_emotion_detection", "-v"]),
        ])
    if any(statuses):
        print("Some checks failed. Review the logs; do not claim they passed.")
        return 1
    print("Requested checks passed. Live Watson checks run only with --live.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
