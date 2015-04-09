
CXXNET=/home/github/cxxnet/bin/cxxnet
PY=pypy
TEST_LIST=
SAMPLE_SUBMISSION=


all: sub.csv


models:
	mkdir models

sub:
	mkdir sub

pred:
	mkdir pred

models/0400.model: models sub pred
	$(CXXNET) ./bn.conf

models/0430.model: models/0400.model
	$(CXXNET) ./bn2.conf

raw_output: models/0430.model
	$(PY) ./run.py $(CXXNET)

sub.csv: raw_output
	$(PY) ../etc/make_sub.py $(SAMPLE_SUBMISSION) $(TEST_LIST) $+ $@
