
CXXNET=/home/github/cxxnet/bin/cxxnet
PY=pypy

all: sub.csv


models:
	mkdir models

sub:
	mkdir sub

pred:
	mkdir pred

models/0267.model: models sub pred
	$(CXXNET) ./val.conf

models/0275.model: models/0267.model
	$(CXXNET) ./val2.conf

raw_output: models/0275.model
	$(PY) ./run.py $(CXXNET)

sub.csv: raw_output
	$(PY) ../etc/make_sub.py $(SAMPLE_SUBMISSION) $(TEST_LIST) $+ $@
