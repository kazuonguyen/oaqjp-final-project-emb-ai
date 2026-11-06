# Final project

## Emotion Detector

A Flask web application that analyzes customer feedback using the embedded
Watson NLP EmotionPredict service. It returns anger, disgust, fear, joy,
sadness, and the dominant emotion.

Starter: https://github.com/ibm-developer-skills-network/oaqjp-final-project-emb-ai

## Run in Skills Network Theia Lab

The course API is accessible only inside the Skills Network Theia Lab.
A local machine can run the web interface, error handling, offline tests,
and Pylint, but cannot complete the real Watson inference checks.

```bash
python3 -m pip install -r requirements.txt
python3 tools/collect_evidence.py --live
python3 -m flask --app server run --host=0.0.0.0 --port=5000
```

Launch the application on port 5000 from the Skills Network toolbox.
Enter `I think I am having fun`, click **Run Sentiment Analysis**, and save
a screenshot with the result as `6b_deployment_test.png`. Clear the input,
click the button again, and save `7c_error_handling_interface.png`.

The original course `templates/index.html` and `static/mywebscript.js` are
retained. The route is `/emotionDetector?textToAnalyze=...`.

## Tests and static analysis

```bash
# Required tests: five real Watson calls, inside Theia Lab
python3 -m unittest test_emotion_detection -v

# Offline regression checks: synthetic HTTP responses, no real inference
python3 -m unittest tests.test_offline -v

# Static analysis, with no disabled checks or custom scoring
python3 -m pylint server.py
```

Invalid or blank text returns six `None` values. A Watson HTTP 400 response
also returns six `None` values. Flask displays `Invalid text! Please try again!`
when `dominant_emotion` is `None`. Network and upstream HTTP failures display
a separate service-unavailable message.

## Verified results (6 November 2026)

- Live Watson imports and required format/package checks passed in Theia.
- All five required live Watson tests passed.
- All 11 offline logic/Flask regression tests passed.
- `pylint server.py` scored **10.00/10** inside Theia.
- Both required deployment/error screenshots are in `evidence/`.

See `SUBMISSION_ANSWERS.md` for all 16 prepared responses.

## Evidence

`python3 tools/collect_evidence.py` creates code snippets and captures actual
local test and lint output in `evidence/`. Add `--live` inside Theia to capture
the task 2, 3, 4, and 5 terminal outputs. Task 2 and task 3 have separate source
snapshots to preserve the raw-response and formatted-response stages.
Failed commands are retained as failures, with their actual exit status.

See `SUBMISSION_GUIDE.md` for the exact evidence mapping and remaining steps.

## License

Apache-2.0, inherited from the IBM starter repository. See `LICENSE`.
