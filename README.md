# 🧪 Testing Project

This project includes:

- ✅ **API tests** using `pytest` and `requests`
- 🌐 **UI tests** using `Selenium`
- ⚙️ **GitHub Actions CI** for running API tests automatically on push

## 📂 Project Structure

- **API tests**: Located in `tests/api/`, covering user creation, updates (PUT/PATCH), deletion, and retrieval.
- **UI tests**: Located in `tests/ui/`, currently not included in CI pipeline.

## ⚙️ Continuous Integration (CI)

- GitHub Actions run API tests automatically on each push to the `main` branch.
- Generates an HTML test report with `pytest-html`.
- Publishes the latest test report to GitHub Pages.

👉 **[📊 View latest test report](https://tany9.github.io/testing_project/)**

---

## 💡 Features

- JSON data-driven API testing
- Self-contained HTML reports
- Modular and scalable test structure

## 🔧 Tools & Technologies

- Python
- Pytest
- Selenium WebDriver
- Requests
- ChromeDriver
- JSON
- GitHub Actions

---

## 🚀 Running Tests Locally

### Install dependencies:

pip install -r requirements.txt

Run API tests with report:
pytest tests/api/ --html=report.html --self-contained-html

Run API tests (verbose mode):
pytest tests/api/ -v

Run UI tests:
pytest tests/ui/ -v


👩‍💻 Author
Project created for learning and portfolio by S.B.