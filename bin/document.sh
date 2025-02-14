
# Adding local symlinks gets nice source locations like
ln -s .venv/lib/python*/site-packages/authx_extra authx_extra

# Build the docs
mkdocs build -d build
