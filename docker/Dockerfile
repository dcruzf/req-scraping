FROM python:3.8

RUN apt-get -y update
RUN apt-get install -y default-jre libhunspell-dev git-lfs build-essential xvfb
RUN git lfs install

COPY . /source

RUN pip install -U pip
RUN pip install Cython
RUN pip install -i https://test.pypi.org/simple/ vlibras-deeplearning --extra-index-url https://pypi.python.org/simple/
RUN pip install -i https://test.pypi.org/simple/ vlibras-translate --extra-index-url https://pypi.python.org/simple/
RUN pip install pandas jupyterlab
RUN pip show vlibras_translate
RUN python -c "from vlibras_translate.translation import Translation as t;t().rule_translation_with_dl('test 1 2 3')"
RUN fairseq-train -h

WORKDIR /code


