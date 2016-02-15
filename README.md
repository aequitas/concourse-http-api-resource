# HTTP Resource

Concourse resource to allow interaction with (simple) HTTP API's.

https://hub.docker.com/r/aequitas/http-resource/

## Source Configuration

Most of the `source` options can also be used in `params` for the specifc actions. This allows to use a different URL path. For example when a POST and GET use different endpoints.

Options set in `params` take precedence over options in `source`.

* `uri`: *Required.* The URI to use for the requests.
    Example: `https://www.hipchat.com/v2/room/1234321/notification`

* `method`: *Optional* Method to use, eg: GET, POST, PATCH (default `GET`).

* `headers`: *Optional* Object containing headers to pass to the request.
    Example:

        headers:
            X-Some-Header: some header content

* `json`: *Optional* JSON to send along with the request.

* `debug`: *Optional* Set debug logging of scripts, takes boolean (default `false`).

## Behavior


### Interpolation

All options support interpolation of variables by using [Python3 formatting](https://docs.python.org/3.5/library/stdtypes.html#str.format)

Build metadata (BUILD_NAME, BUILD_JOB_NAME, BUILD_PIPELINE_NAME and BUILD_ID) are currently the only available values.

## Examples

### Post notification on HipChat

```yaml
resources:
    - name: hipchat
      type: http
      source:
          uri: https://www.hipchat.com/v2/room/team_room/notification
          method: POST
          headers:
              Authorization: Bearer {{HIPCHAT_TOKEN}}

jobs:
    - name: Test and notify
      plan:
          - task: build
            file: ci/build.yaml
            on_success:
                put: hipchat
                params:
                    json:
                        color: green
                        message: Build {BUILD_PIPELINE_NAME}{BUILD_JOB_NAME}, nr: {BUILD_NAME} was a success!
            on_failure:
                put: hipchat
                params:
                    json:
                        color: red
                        message: Build {BUILD_PIPELINE_NAME}{BUILD_JOB_NAME}, nr: {BUILD_NAME} failed horribly!


```
