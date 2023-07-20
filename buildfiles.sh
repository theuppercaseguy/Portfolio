echo "BUILD START"


python3.9 -m pip install -r requirements.txt
python3.9 -m manage.py collectstatic --noinout --clear    









echo "BUILD END"