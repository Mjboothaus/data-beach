FROM condaforge/mambaforge
ENV SHELL /bin/bash
ADD environment.yaml .
RUN mamba env create -n databooth -f conda_environment.yaml
