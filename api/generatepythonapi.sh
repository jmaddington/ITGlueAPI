docker run --rm \
  -v ${PWD}:/local \
  -v "${PWD}/../openapi.yml:/local/openapi.yml" \
  openapitools/openapi-generator-cli generate \
  -i /local/openapi.yml \
  -g python \
  -o /local/api