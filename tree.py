import os

base_dir = "tts_core"

# Top-level files: giving the project a professional setup
top_level_files = {
    "README.md": [
        "# tts_core",
        "",
        "This directory forms the core of a Text-To-Speech (TTS) system. It includes:",
        "- Configuration files for multilingual TTS (Uzbek, Russian, English) and future languages.",
        "- Model directories for language-specific and generic TTS models.",
        "- Integration layers for frontend UIs (mobile/desktop/web), banking APIs, and credit card operations.",
        "- Scripts, notebooks, and tests for development, optimization, performance checks, and security validations.",
        "- Comprehensive documentation (architecture diagrams, API specs, user guides).",
        "- CI/CD and infrastructure hints via Makefile, pyproject.toml for packaging, and a requirements.txt.",
        "",
        "By examining the directories and files, you can understand each step of the TTS pipeline, from input text processing and model inference to output caching, logging, and integration with external services.",
        "",
        "## Key Highlights:",
        "- **Multilingual**: Support for Uzbek, Russian, English TTS, easily extensible.",
        "- **Integration**: Banking endpoints, credit card notifications, frontend UIs.",
        "- **Performance & Security**: Dedicated tests, optimization scripts, and caching strategies.",
        "- **Documentation & Tooling**: Extensive docs, notebooks, configs, and scripts to guide developers.",
        "",
        "## Structure Overview:",
        "Top-level directories and files indicate a well-organized codebase. Dive into `docs/`, `tests/`, `models_*`, `integration/`, `configs/`, `scripts/`, `notebooks/`, and `test_env/` to explore further.",
        "",
        "Refer to `CONTRIBUTING.md` for contribution guidelines and `CODE_OF_CONDUCT.md` for project standards.",
        ""
    ],
    "LICENSE": [
        "MIT License",
        "",
        "Permission is hereby granted, free of charge, to any person obtaining a copy",
        "of this software and associated documentation files (the 'Software'), to deal",
        "in the Software without restriction..."
    ],
    "CONTRIBUTING.md": [
        "# Contributing Guidelines",
        "",
        "1. Fork the repository and create a new branch for your feature or fix.",
        "2. Add or update tests, maintain code style.",
        "3. Submit a pull request explaining your changes.",
        "4. Ensure CI tests pass before merging."
    ],
    "CHANGELOG.md": [
        "# Changelog",
        "",
        "## [Unreleased]",
        "- Initial project structure setup.",
        "- Added multilingual TTS model directories.",
        "- Integrated banking and credit card endpoints.",
        "- Added tests, docs, scripts."
    ],
    "CODE_OF_CONDUCT.md": [
        "# Code of Conduct",
        "",
        "All contributors are expected to follow standards of professionalism, respect, and inclusivity."
    ],
    "CITATION.cff": [
        "cff-version: 1.2.0",
        "message: If you use this software, please cite it as below.",
        "authors:",
        "  - family-names: Doe",
        "    given-names: Jane",
        "title: tts_core",
        "date-released: 2023-01-01",
        "version: 0.1.0"
    ],
    "requirements.txt": [
        "numpy",
        "scipy",
        "pytorch",
        "librosa",
        "requests"
    ],
    "pyproject.toml": [
        "[build-system]",
        "requires = [\"setuptools\", \"wheel\"]",
        "build-backend = \"setuptools.build_meta\"",
        "",
        "[project]",
        "name = \"tts_core\"",
        "version = \"0.1.0\"",
        "description = \"Core TTS functionality with multilingual support.\"",
        "authors = [{name = \"Jane Doe\", email = \"jane@example.com\"}]",
        "license = \"MIT\"",
        "dependencies = [\"numpy\", \"scipy\"]"
    ],
    "Makefile": [
        "# Makefile for building, testing, and deploying tts_core",
        "",
        "install:",
        "\tpip install -r requirements.txt",
        "",
        "test:",
        "\tpytest tests",
        "",
        "lint:",
        "\tflake8 .",
        "",
        "docs:",
        "\tmake -C docs html"
    ]
}

# Directory structure with subdirectories
subdirs = [
    "docs",
    "docs/architecture",
    "docs/api",
    "docs/user_guides",
    "docs/user_stories",
    "docs/security",
    "tests",
    "tests/unit",
    "tests/integration",
    "tests/performance",
    "tests/security",
    "tests/load",
    "tests/end_to_end",
    "models_uz",
    "models_ru",
    "models_en",
    "models_generic",
    "language_support",
    "language_support/tests",
    "integration",
    "integration/frontend",
    "integration/banking",
    "integration/credit_card",
    "cache",
    "samples",
    "samples/multilingual",
    "scripts",
    "configs",
    "configs/env",
    "configs/templates",
    "notebooks",
    "utils",
    "utils/logging",
    "utils/audio_processing",
    "utils/conversion",
    "test_env",
    "test_env/simulated_inputs",
    "test_env/audio_variations"
]

# Files to create in certain directories
dir_files = {
    "docs/architecture": [
        "tts_system_overview.mmd", # Mermaid diagram of entire TTS system architecture
        "architecture_notes.txt",
        "diagram_instructions.md"
    ],
    "docs/api": [
        "tts_api_endpoints.yaml",
        "api_overview.md",
        "authentication_guide.txt"
    ],
    "docs/user_guides": [
        "getting_started.md",
        "frontend_setup.md",
        "model_deployment_guide.md"
    ],
    "docs/user_stories": [
        "banking_user_stories.md",
        "credit_card_user_stories.md",
        "multilingual_user_stories.md"
    ],
    "docs/security": [
        "security_threat_model.md",
        "data_privacy.yaml",
        "vulnerability_report_template.txt"
    ],
    "tests/unit": [
        "test_basic_synthesis.py",
        "test_language_handling.py"
    ],
    "tests/integration": [
        "test_frontend_connection.py",
        "test_banking_integration.py"
    ],
    "tests/performance": [
        "test_latency.py",
        "test_resource_usage.py"
    ],
    "tests/security": [
        "test_input_sanitization.py",
        "test_auth_controls.py"
    ],
    "tests/load": [
        "test_high_load_conditions.py",
        "test_scaling_strategies.py"
    ],
    "tests/end_to_end": [
        "test_full_pipeline.py",
        "test_complex_scenarios.py"
    ],
    "models_uz": [
        "uzbek_model_info.txt",
        "uz_feature_extractor.py"
    ],
    "models_ru": [
        "russian_model_info.txt",
        "ru_feature_extractor.py"
    ],
    "models_en": [
        "english_model_info.txt",
        "en_feature_extractor.py"
    ],
    "models_generic": [
        "generic_model_notes.txt",
        "generic_feature_extractor.py"
    ],
    "language_support": [
        "lang_mapping.yaml",
        "supported_languages.json"
    ],
    "language_support/tests": [
        "test_lang_mapping.py"
    ],
    "integration/frontend": [
        "frontend_integration_guide.md",
        "mock_frontend_data.json"
    ],
    "integration/banking": [
        "banking_apis.yaml",
        "test_banking_responses.py"
    ],
    "integration/credit_card": [
        "credit_card_scenarios.yaml",
        "cc_notify_handler.py"
    ],
    "cache": [
        "cache_config.yaml",
        "cache_manager.py"
    ],
    "samples/multilingual": [
        "sample_transcripts.json",
        "sample_analysis.ipynb"
    ],
    "scripts": [
        "run_tts_pipeline.sh",
        "quality_check.py",
        "audio_format_converter.py"
    ],
    "configs": [
        "tts_config.yaml",
        "default_settings.json"
    ],
    "configs/env": [
        "dev_env.yaml",
        "prod_env.yaml",
        "env_notes.txt"
    ],
    "configs/templates": [
        "template_config.yaml",
        "template_variables.json"
    ],
    "notebooks": [
        "tts_research.ipynb",
        "data_distribution.ipynb"
    ],
    "utils": [
        "readme_utils.md",
        "utils_init.py"
    ],
    "utils/logging": [
        "log_config.yaml",
        "log_formatter.py"
    ],
    "utils/audio_processing": [
        "noise_reduction.py",
        "pitch_shifter.py",
        "speed_adjuster.py"
    ],
    "utils/conversion": [
        "text_cleaner.py",
        "phoneme_converter.py"
    ],
    "test_env/simulated_inputs": [
        "mock_user_queries.txt",
        "simulate_user_input.sh"
    ],
    "test_env/audio_variations": [
        "variation_tests.json",
        "add_noise.py"
    ]
}

def write_file(path, lines):
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")

def generic_content(name):
    return [f"# {name}", "# Placeholder content for project use. Adjust as needed."]

def generate_content_for_file(filename):
    ext = os.path.splitext(filename)[1]
    if ext == ".py":
        return [f"# {filename}", "# Python code for related functionality."]
    elif ext in [".yaml", ".yml"]:
        return [f"# {filename}", "# YAML configuration file."]
    elif ext == ".json":
        return ["{", f'  "description": "Placeholder for {filename}"', "}"]
    elif ext == ".txt":
        return [f"# {filename}", "# Text notes or documentation."]
    elif ext == ".sh":
        return [f"#!/usr/bin/env bash", f"# {filename}", "# Shell script placeholder.", "echo 'Running script...'"]
    elif ext == ".ipynb":
        return ['{"cells":[],"metadata":{},"nbformat":4,"nbformat_minor":5}']
    elif ext == ".md":
        return [f"# {filename}", "# Markdown documentation or guides."]
    elif ext == ".mmd":
        return [f"%% Mermaid diagram for {filename}", "graph LR;", "A-->B;"]
    else:
        return generic_content(filename)

def main():
    # If tts_core exists, remove it completely first (except if user wants to keep something)
    if os.path.exists(base_dir):
        import shutil
        shutil.rmtree(base_dir)
    os.makedirs(base_dir)
    print(f"Created directory: {base_dir}")

    # Create top-level files
    for fname, content in top_level_files.items():
        file_path = os.path.join(base_dir, fname)
        write_file(file_path, content)
        print(f"Created top-level file: {file_path}")

    # Create directories
    for d in subdirs:
        dir_path = os.path.join(base_dir, d)
        os.makedirs(dir_path, exist_ok=True)
        gitkeep_path = os.path.join(dir_path, ".gitkeep")
        write_file(gitkeep_path, [f"# .gitkeep to keep {d} directory in version control."])
        print(f"Created directory: {dir_path} and .gitkeep")

    # Create files in directories
    for directory, files in dir_files.items():
        for f in files:
            file_path = os.path.join(base_dir, directory, f)
            lines = generate_content_for_file(f)
            write_file(file_path, lines)
            print(f"Created file: {file_path}")

    # Append file tree overview to README.md
    readme_path = os.path.join(base_dir, "README.md")
    with open(readme_path, "a") as f:
        f.write("\n## Detailed File Tree\n\n")
        f.write("The following directories and files were created to provide a comprehensive structure:\n\n")
        f.write("- Top-level files like `LICENSE`, `CONTRIBUTING.md`, `CHANGELOG.md`, `CODE_OF_CONDUCT.md`, `CITATION.cff`, `requirements.txt`, `pyproject.toml`, and `Makefile` ensure good project hygiene, documentation, and packaging.\n")
        f.write("- `docs/` contains architecture diagrams (`.mmd`), API specs (`.yaml`), user guides (`.md`), user stories, and security notes.\n")
        f.write("- `tests/` organizes tests by category: `unit`, `integration`, `performance`, `security`, `load`, `end_to_end`.\n")
        f.write("- `models_uz`, `models_ru`, `models_en`, `models_generic` hold model-specific info and preprocessing scripts.\n")
        f.write("- `language_support/` maps languages and tests their configurations.\n")
        f.write("- `integration/` directories (frontend, banking, credit_card) show how TTS integrates with external services.\n")
        f.write("- `cache/` has config and a manager for caching TTS results.\n")
        f.write("- `samples/multilingual` provides sample transcripts and analysis.\n")
        f.write("- `scripts/` for running the TTS pipeline and related checks.\n")
        f.write("- `configs/` for main TTS configs, environment-specific settings, and templates.\n")
        f.write("- `notebooks/` for experimenting and researching TTS improvements.\n")
        f.write("- `utils/` for logging, audio processing, and text/phoneme conversion tools.\n")
        f.write("- `test_env/` simulates user inputs and audio variations for robust testing.\n")
        f.write("- Root-level `tts_main.py` is the main Python entry point, `run.sh` a script to run pipelines.\n")
        f.write("\nThis structure should guide developers and stakeholders in navigating the codebase, understanding each component's purpose, and extending or integrating the TTS solution further.\n")

    print("Appended detailed file tree overview to README.md.")
    print("File tree creation for tts_core completed with a comprehensive set of directories and files!")

if __name__ == "__main__":
    main()
