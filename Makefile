# --- --- ---

install:
	@python3 -m pip install -r requirements.txt

update:
	git pull
	sudo supervisorctl restart twon-api

test:
	@python -m pytest tests/


# --- --- ---

dev:
	@python -m uvicorn api:app --reload

serve:
	@python -m uvicorn api:app
