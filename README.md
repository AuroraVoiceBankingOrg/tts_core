# tts_core
TTS core: Convert text answers to speech in multiple languages. Easy to add new languages, optimize latency. Integrate with frontends, banking info readouts. Supports cloud or local model storage. Perfect for voice-based banking operations.

## High-Level Idea and Integration with Other Repositories

**Overall System Context:**  
This TTS (Text-To-Speech) component (`tts_core`) is part of a larger AI voice assistant ecosystem. The entire system typically handles:
1. **Input** (voice or text) from the user.
2. **ASR (Automatic Speech Recognition)** if the input is voice (handled by `asr_core` repository).
3. **NLU/LLM (Natural Language Understanding/Large Language Model)** to interpret the user’s query (handled by `ai_nlu` or integrated LLM services).
4. **External Integrations** with banking APIs, credit card processors, and multiple database backends for retrieving user account info, performing transactions, etc. (handled by `external_integrations`).
5. **Conversation Flow Management** to maintain context, recall past queries, and route requests (handled by `conversation_flow`).
6. **Configuration Management** for loading environment-specific, language-specific, and performance-related settings (handled by `config_manager`).
7. **Frontends** (mobile, desktop, web) integration and UI (provided by `frontend_integrations`), where the user interacts.
8. **Testing and Evaluation** frameworks (provided by `testing_envs`, `evaluation`, and integrated scripts) to ensure the system meets performance, latency, and quality targets.

**Where `tts_core` Fits In:**  
When the system has determined the user’s intent and fetched the requested data, it needs to respond. If the user wants a voice response, `tts_core` comes into play. `tts_core`:
- Loads the appropriate TTS model for the language in which the response should be given (e.g., Uzbek, Russian, English).
- Applies pitch, speed adjustments, and possibly cloud-based services if needed.
- Integrates with caching to avoid regenerating the same responses repeatedly.
- Interacts with the frontend integration layer so the synthesized speech can be delivered to the user’s device.

Thus, `tts_core` is invoked towards the end of the processing chain, turning a textual answer into natural-sounding speech.

---

## Running Order Inside the Project

**Typical Runtime Flow:**
1. **Initialization**:  
   `main.py` (in `tts_core`) might not be the global system entry point; rather, it’s a central script for TTS operations. The global entry might be in another repo (like `core_repo/main.py`). However, if this `tts_core` repo is run independently for testing or development:
   - `main.py` loads configurations from `configs/` (e.g., `tts_config.yaml`) to determine model paths, languages, performance settings.
   - It initializes logging (via `utils/logging/` configs), sets up audio processing utilities (`utils/audio_processing`), and text/phoneme conversion tools (`utils/conversion`).
   - It may preload or lazy-load TTS models from `models_uz/`, `models_ru/`, `models_en/`, or `models_generic/`.

2. **Request Handling**:  
   When a text answer is provided by upstream logic (NLU/LLM, banking data from `external_integrations`, etc.), `tts_core`:
   - Selects the correct language model based on `language_support/lang_mapping.yaml` and `supported_languages.json`.
   - If caching is enabled, `cache/` logic checks if this response was generated before to speed up the reply.
   - Uses `integration` directories to apply any required frontend formatting or banking/credit card response formatting before synthesis.

3. **Synthesis Process**:  
   A TTS model (e.g., from `models_uz/uz_feature_extractor.py` and the model files) synthesizes speech. `optimization/` scripts and configs ensure this step is efficient, possibly reducing latency below the 150-200ms target.

4. **Output Delivery**:  
   The synthesized audio is either returned directly to the calling system or stored in a temporary location. If a frontend is connected (`integration/frontend`), the output is transferred or streamed to the user’s device. For banking/credit card scenarios, special prompts or confirmations defined in `integration/banking` and `integration/credit_card` ensure compliance and clarity.

5. **Logging & Testing**:  
   Logs are recorded (`utils/logging/`, `logs/`) for debugging and performance checks. Test scenarios in `tests/` and `test_env/` can be run to ensure everything works as expected. Notebooks in `notebooks/` help developers analyze TTS quality and data distribution.

---

## Detailed Visual Flow

**Visual Flow Diagram (Conceptual):**

```
         ┌───────────────────┐
         │  conversation_flow │
         │   (from other repo)│
         └───────▲───────────┘
                 │Text response determined
                 │
                 ▼
            ┌──────────┐
            │ config_mgr│   # load TTS configs
            └────▲─────┘
                 │
       (If voice needed)
                 │
                 ▼
            ┌───────────┐    # choose language
            │ language_  │    # check lang_mapping.yaml
            │ support/    │
            └────▲────────┘
                 │
                 ▼
           ┌─────────┐     # checks cache_config.yaml
           │  cache/  │     # cache_manager.py sees if response was cached
           └────▲─────┘
                 │ (miss)
                 │(if cached, skip synthesis)
                 ▼
           ┌─────────────┐
           │  models_*/   │   # load correct language model files,
           │ feature_*.py │   # do phoneme conv.
           └─────▲────────┘
                 │
                 ▼
          ┌────────────────┐
          │    utils/      │   # noise_reduction.py, pitch_shifter.py if needed
          │ audio_processing│
          └───────▲────────┘
                 │
                 ▼
          ┌────────────────┐
          │   scripts/     │  # run_tts_pipeline.sh, or quality_check.py if needed
          └───────▲────────┘
                 │(done)
                 ▼ Synthesized Audio
        ┌─────────────────┐
        │ integration/     │   # If needed, integrate with frontend or banking endpoints
        │ (frontend,banking│   # adjusting final output or sending through APIs
        │  credit_card)    │
        └───────▲─────────┘
                │
                ▼
             Audio delivered back
             to conversation flow or
             directly to frontends
```

In a combined scenario, `tts_core` would be called by `conversation_flow` after `asr_core` and `ai_nlu` steps are done. The `evaluation`, `testing_envs`, and `utils_infra` repos can run in parallel or be triggered by CI/CD pipelines to ensure ongoing performance and quality.

---

## File Tree with Comments Next to Each File

`tts_core/` (root):
- `README.md`: Explains what `tts_core` does, how to use it, and how it integrates.
- `LICENSE`: Licensing info (MIT).
- `CONTRIBUTING.md`: Guidelines for contributing.
- `CHANGELOG.md`: Historical record of changes.
- `CODE_OF_CONDUCT.md`: Behavioral standards for contributors.
- `CITATION.cff`: How to cite this project in academic works.
- `requirements.txt`: Basic dependencies for TTS operation (numpy, scipy, pytorch, etc.).
- `pyproject.toml`: Build and project metadata for packaging.
- `Makefile`: Convenient commands for install, test, lint, docs.

`docs/`: Documentation
- `docs/architecture/`:
  - `tts_system_overview.mmd`: Mermaid diagram of TTS system architecture.
  - `architecture_notes.txt`: Text notes explaining architectural decisions.
  - `diagram_instructions.md`: Instructions on generating and reading diagrams.
- `docs/api/`:
  - `tts_api_endpoints.yaml`: YAML listing TTS-related API endpoints.
  - `api_overview.md`: Markdown overview of TTS API functionalities.
  - `authentication_guide.txt`: Steps for authenticating if TTS service requires tokens.
- `docs/user_guides/`:
  - `getting_started.md`: How to set up and run basic TTS tasks.
  - `frontend_setup.md`: Integrating TTS outputs with frontend UIs.
  - `model_deployment_guide.md`: How to deploy models in production.
- `docs/user_stories/`:
  - `banking_user_stories.md`: Scenarios where users ask for bank info.
  - `credit_card_user_stories.md`: Handling credit card notifications vocally.
  - `multilingual_user_stories.md`: Examples of users interacting in multiple languages.
- `docs/security/`:
  - `security_threat_model.md`: Security considerations in TTS processing.
  - `data_privacy.yaml`: YAML specifying data privacy measures.
  - `vulnerability_report_template.txt`: Template for reporting found vulnerabilities.

`tests/`: Organized testing approach
- `tests/unit/`:
  - `test_basic_synthesis.py`: Test basic TTS synthesis functionality.
  - `test_language_handling.py`: Test language selection logic.
- `tests/integration/`:
  - `test_frontend_connection.py`: Ensure TTS audio reaches frontend simulation correctly.
  - `test_banking_integration.py`: Check that TTS responses include correct banking info.
- `tests/performance/`:
  - `test_latency.py`: Measure and ensure latency stays within targets.
  - `test_resource_usage.py`: Confirm acceptable CPU/RAM usage.
- `tests/security/`:
  - `test_input_sanitization.py`: Ensure inputs are sanitized to avoid injection attacks.
  - `test_auth_controls.py`: Validate any necessary authentication for TTS services.
- `tests/load/`:
  - `test_high_load_conditions.py`: Test TTS under heavy concurrency/load.
  - `test_scaling_strategies.py`: Ensure horizontal scaling or caching strategies work.
- `tests/end_to_end/`:
  - `test_full_pipeline.py`: Simulate full user request from text to speech output.
  - `test_complex_scenarios.py`: End-to-end tests with complex queries and conditions.

`models_uz/`, `models_ru/`, `models_en/`: 
- Each contains model-specific info and feature extractors:
  - e.g., `uz_feature_extractor.py` interprets Uzbek linguistic features for TTS.
  - `*.txt` files hold notes about model versions, tuning steps.

`models_generic/`:
- `generic_model_notes.txt`: General TTS model notes.
- `generic_feature_extractor.py`: Code for model-agnostic features.

`language_support/`:
- `lang_mapping.yaml`: Maps language codes (e.g. 'uz', 'ru', 'en') to model directories.
- `supported_languages.json`: Lists languages currently supported.
- `language_support/tests/test_lang_mapping.py`: Tests that language mappings are correct.

`integration/`: Show how TTS integrates with external services
- `integration/frontend/`:
  - `frontend_integration_guide.md`: Steps to connect TTS outputs to frontends.
  - `mock_frontend_data.json`: Example frontend UI payloads.
- `integration/banking/`:
  - `banking_apis.yaml`: Config for banking API endpoints.
  - `test_banking_responses.py`: Tests to ensure TTS incorporates banking info correctly.
- `integration/credit_card/`:
  - `credit_card_scenarios.yaml`: YAML describing credit card notification scenarios.
  - `cc_notify_handler.py`: Code for formatting credit card alerts into speech.

`cache/`:
- `cache_config.yaml`: Configuration for caching results.
- `cache_manager.py`: Python code to handle cache loading, storing TTS outputs.

`samples/multilingual/`:
- `sample_transcripts.json`: Example transcripts for multiple languages.
- `sample_analysis.ipynb`: Notebook analyzing sample transcripts quality.

`scripts/`:
- `run_tts_pipeline.sh`: Shell script to run the entire TTS pipeline (from config load to output).
- `quality_check.py`: Python tool checking audio quality of TTS outputs.
- `audio_format_converter.py`: Convert audio outputs into desired formats.

`configs/`:
- `tts_config.yaml`: Main TTS configuration (model paths, languages, pitch/speed defaults).
- `default_settings.json`: Fallback settings if env-specific configs not found.
- `configs/env/`:
  - `dev_env.yaml`: Development environment overrides.
  - `prod_env.yaml`: Production environment overrides.
  - `env_notes.txt`: Notes on environment differences.
- `configs/templates/`:
  - `template_config.yaml`: A template for generating custom configs.
  - `template_variables.json`: Variables for use in templates.

`notebooks/`:
- `tts_research.ipynb`: Researching advanced TTS features, voice tuning.
- `data_distribution.ipynb`: Analyze distribution of input text and output audio characteristics.

`utils/`:
- `readme_utils.md`: Explains what utilities are available.
- `utils_init.py`: Initialization code for utilities.
- `utils/logging/`:
  - `log_config.yaml`: YAML configuring log format, level.
  - `log_formatter.py`: Python code customizing log formatting.
- `utils/audio_processing/`:
  - `noise_reduction.py`: Apply noise reduction to output audio.
  - `pitch_shifter.py`: Adjust pitch for certain voice styles.
  - `speed_adjuster.py`: Alter speech rate if needed.
- `utils/conversion/`:
  - `text_cleaner.py`: Clean input text before synthesis.
  - `phoneme_converter.py`: Convert text to phonemes for TTS models.

`test_env/`:
- `test_env/simulated_inputs/`:
  - `mock_user_queries.txt`: Simulated user queries (e.g., “What’s my balance?”)
  - `simulate_user_input.sh`: Script to replay these queries as if from a frontend.
- `test_env/audio_variations/`:
  - `variation_tests.json`: Specifies scenarios of adding noise, changes in pitch to test robustness.
  - `add_noise.py`: Adds controlled noise to test TTS resilience.
