# tts_core

This directory forms the core of a Text-To-Speech (TTS) system. It includes:
- Configuration files for multilingual TTS (Uzbek, Russian, English) and future languages.
- Model directories for language-specific and generic TTS models.
- Integration layers for frontend UIs (mobile/desktop/web), banking APIs, and credit card operations.
- Scripts, notebooks, and tests for development, optimization, performance checks, and security validations.
- Comprehensive documentation (architecture diagrams, API specs, user guides).
- CI/CD and infrastructure hints via Makefile, pyproject.toml for packaging, and a requirements.txt.

By examining the directories and files, you can understand each step of the TTS pipeline, from input text processing and model inference to output caching, logging, and integration with external services.

## Key Highlights:
- **Multilingual**: Support for Uzbek, Russian, English TTS, easily extensible.
- **Integration**: Banking endpoints, credit card notifications, frontend UIs.
- **Performance & Security**: Dedicated tests, optimization scripts, and caching strategies.
- **Documentation & Tooling**: Extensive docs, notebooks, configs, and scripts to guide developers.

## Structure Overview:
Top-level directories and files indicate a well-organized codebase. Dive into `docs/`, `tests/`, `models_*`, `integration/`, `configs/`, `scripts/`, `notebooks/`, and `test_env/` to explore further.

Refer to `CONTRIBUTING.md` for contribution guidelines and `CODE_OF_CONDUCT.md` for project standards.


## Detailed File Tree

The following directories and files were created to provide a comprehensive structure:

- Top-level files like `LICENSE`, `CONTRIBUTING.md`, `CHANGELOG.md`, `CODE_OF_CONDUCT.md`, `CITATION.cff`, `requirements.txt`, `pyproject.toml`, and `Makefile` ensure good project hygiene, documentation, and packaging.
- `docs/` contains architecture diagrams (`.mmd`), API specs (`.yaml`), user guides (`.md`), user stories, and security notes.
- `tests/` organizes tests by category: `unit`, `integration`, `performance`, `security`, `load`, `end_to_end`.
- `models_uz`, `models_ru`, `models_en`, `models_generic` hold model-specific info and preprocessing scripts.
- `language_support/` maps languages and tests their configurations.
- `integration/` directories (frontend, banking, credit_card) show how TTS integrates with external services.
- `cache/` has config and a manager for caching TTS results.
- `samples/multilingual` provides sample transcripts and analysis.
- `scripts/` for running the TTS pipeline and related checks.
- `configs/` for main TTS configs, environment-specific settings, and templates.
- `notebooks/` for experimenting and researching TTS improvements.
- `utils/` for logging, audio processing, and text/phoneme conversion tools.
- `test_env/` simulates user inputs and audio variations for robust testing.
- Root-level `tts_main.py` is the main Python entry point, `run.sh` a script to run pipelines.

This structure should guide developers and stakeholders in navigating the codebase, understanding each component's purpose, and extending or integrating the TTS solution further.
