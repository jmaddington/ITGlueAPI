docker run --rm \
  -v ${PWD}:/local \
  -v "${PWD}/../itglue.yml:/local/itglue.yml" \
  openapitools/openapi-generator-cli generate \
  -i /local/itglue.yml \
  -g python \
  -o /local/python/api