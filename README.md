# IT Glue OpenAPI
IT Glue's API in an OpenAPI (Swagger) Format.

___This is a work in progress__

It is generated with a combination of automation and manual work.

## Requirements
The generated python API is included.

If you want to generate it again or output  a different language your options are to
edit `generatepythonapi.yaml` and replace these lines with whatever you need:
```bash
  -g python \
  -o /local/python/api
```

This script uses docker. However, the generator is also available with homebrew on macOS
and on npm, [see the OpenAPI docs here](https://openapi-generator.tech/docs/installation)

## Contributing
Fork the repository and then issue a pull request.

If you don't know what that means, make appropriate changes and email me at jonathan.addington@jmaddington.com