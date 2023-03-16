echo "Validating itglue.yaml"

valid=`swagger-cli validate itglue.yaml`

# Check if the string contains "is valid"
if [[ $valid == *"is valid"* ]]; then
  echo "Valid OpenAPI YAML"
else
  echo "There is a problem with the OpenAPI YAML. Please fix it and try again."
  exit 1
fi

docker run --rm \
  -v ${PWD}:/local \
  -v "${PWD}/../itglue.yaml:/local/itglue.yaml" \
  openapitools/openapi-generator-cli generate \
  -i /local/itglue.yaml \
  --package-name itglue \
  -g python \
  -o /local/python/api

exit 0