.PHONY: unit
unit:
	poetry run python -m pytest -s tests/unit
