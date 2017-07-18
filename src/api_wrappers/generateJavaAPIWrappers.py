#!/usr/bin/env python2.7
#
# Copyright (C) 2013-2016 DNAnexus, Inc.
#
# This file is part of dx-toolkit (DNAnexus platform client libraries).
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may not
#   use this file except in compliance with the License. You may obtain a copy
#   of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.

import sys, json

preamble = '''/* Do not modify this file by hand.
 *
 * It is automatically generated by src/api_wrappers/generateJavaAPIWrappers.py.
 * (Run make api_wrappers to update it.)
 */

package com.dnanexus;

import com.dnanexus.DXHTTPRequest.RetryStrategy;
import com.dnanexus.exceptions.DXAPIException;
import com.dnanexus.exceptions.DXHTTPException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

/**
 * Utility class containing low-level wrappers for invoking DNAnexus API methods.
 */
public final class DXAPI {

    // Utility class should not be instantiated
    private DXAPI() {
    }

    private static ObjectMapper mapper = new ObjectMapper();
'''

postscript = '''}
'''

class_method_template = '''
    /**
     * Invokes the {method_name} method with an empty input, deserializing to an object of the specified class.{wiki_link}
     *
     * @param outputClass class to deserialize the server reponse to
     *
     * @return Server response parsed from JSON
     *
     * @throws DXAPIException
     *             If the server returns a complete response with an HTTP status
     *             code other than 200 (OK).
     * @throws DXHTTPException
     *             If an error occurs while making the HTTP request or obtaining
     *             the response (includes HTTP protocol errors).
     */
    public static <T> T {method_name}(Class<T> outputClass) {{
        return {method_name}(mapper.createObjectNode(), outputClass);
    }}
    /**
     * Invokes the {method_name} method with an empty input using the specified environment, deserializing to an object of the specified class.{wiki_link}
     *
     * @param outputClass class to deserialize the server reponse to
     * @param env environment object specifying the auth token and remote server and protocol
     *
     * @return Server response parsed from JSON
     *
     * @throws DXAPIException
     *             If the server returns a complete response with an HTTP status
     *             code other than 200 (OK).
     * @throws DXHTTPException
     *             If an error occurs while making the HTTP request or obtaining
     *             the response (includes HTTP protocol errors).
     */
    public static <T> T {method_name}(Class<T> outputClass, DXEnvironment env) {{
        return {method_name}(mapper.createObjectNode(), outputClass, env);
    }}
    /**
     * Invokes the {method_name} method with the specified input, deserializing to an object of the specified class.{wiki_link}
     *
     * @param inputObject input object (to be JSON serialized to an input hash)
     * @param outputClass class to deserialize the server reponse to
     *
     * @return Server response parsed from JSON
     *
     * @throws DXAPIException
     *             If the server returns a complete response with an HTTP status
     *             code other than 200 (OK).
     * @throws DXHTTPException
     *             If an error occurs while making the HTTP request or obtaining
     *             the response (includes HTTP protocol errors).
     */
    public static <T> T {method_name}(Object inputObject, Class<T> outputClass) {{
        {input_code}
        return DXJSON.safeTreeToValue(
                new DXHTTPRequest().request("{route}", input, {retry_strategy_with_nonce}),
                outputClass);
    }}
    /**
     * Invokes the {method_name} method with the specified input using the specified environment, deserializing to an object of the specified class.{wiki_link}
     *
     * @param inputObject input object (to be JSON serialized to an input hash)
     * @param outputClass class to deserialize the server reponse to
     * @param env environment object specifying the auth token and remote server and protocol
     *
     * @return Server response parsed from JSON
     *
     * @throws DXAPIException
     *             If the server returns a complete response with an HTTP status
     *             code other than 200 (OK).
     * @throws DXHTTPException
     *             If an error occurs while making the HTTP request or obtaining
     *             the response (includes HTTP protocol errors).
     */
    public static <T> T {method_name}(Object inputObject, Class<T> outputClass, DXEnvironment env) {{
        {input_code}
        return DXJSON.safeTreeToValue(
                new DXHTTPRequest(env).request("{route}", input, {retry_strategy_with_nonce}),
                outputClass);
    }}

    /**
     * Invokes the {method_name} method.{wiki_link}
     *
     * @return Server response parsed from JSON
     *
     * @throws DXAPIException
     *             If the server returns a complete response with an HTTP status
     *             code other than 200 (OK).
     * @throws DXHTTPException
     *             If an error occurs while making the HTTP request or obtaining
     *             the response (includes HTTP protocol errors).
     *
     * @deprecated Use {{@link #{method_name}(Class)}} instead and supply your own class to deserialize to.
     */
    @Deprecated
    public static JsonNode {method_name}() {{
        return {method_name}(mapper.createObjectNode());
    }}
    /**
     * Invokes the {method_name} method with the specified input parameters.{wiki_link}
     *
     * @param inputParams input parameters to the API call
     *
     * @return Server response parsed from JSON
     *
     * @throws DXAPIException
     *             If the server returns a complete response with an HTTP status
     *             code other than 200 (OK).
     * @throws DXHTTPException
     *             If an error occurs while making the HTTP request or obtaining
     *             the response (includes HTTP protocol errors).
     *
     * @deprecated Use {{@link #{method_name}(Object, Class)}} instead and supply your own class to deserialize to.
     */
    @Deprecated
    public static JsonNode {method_name}(JsonNode inputParams) {{
        return new DXHTTPRequest().request("{route}", inputParams, {retry_strategy});
    }}
    /**
     * Invokes the {method_name} method with the specified environment.{wiki_link}
     *
     * @param env environment object specifying the auth token and remote server and protocol
     *
     * @return Server response parsed from JSON
     *
     * @throws DXAPIException
     *             If the server returns a complete response with an HTTP status
     *             code other than 200 (OK).
     * @throws DXHTTPException
     *             If an error occurs while making the HTTP request or obtaining
     *             the response (includes HTTP protocol errors).
     *
     * @deprecated Use {{@link #{method_name}(Class, DXEnvironment)}} instead and supply your own class to deserialize to.
     */
    @Deprecated
    public static JsonNode {method_name}(DXEnvironment env) {{
        return {method_name}(mapper.createObjectNode(), env);
    }}
    /**
     * Invokes the {method_name} method with the specified environment and input parameters.{wiki_link}
     *
     * @param inputParams input parameters to the API call
     * @param env environment object specifying the auth token and remote server and protocol
     *
     * @return Server response parsed from JSON
     *
     * @throws DXAPIException
     *             If the server returns a complete response with an HTTP status
     *             code other than 200 (OK).
     * @throws DXHTTPException
     *             If an error occurs while making the HTTP request or obtaining
     *             the response (includes HTTP protocol errors).
     *
     * @deprecated Use {{@link #{method_name}(Object, Class, DXEnvironment)}} instead and supply your own class to deserialize to.
     */
    @Deprecated
    public static JsonNode {method_name}(JsonNode inputParams, DXEnvironment env) {{
        return new DXHTTPRequest(env).request("{route}", inputParams, {retry_strategy});
    }}'''

object_method_template = '''
    /**
     * Invokes the {method_name} method with an empty input, deserializing to an object of the specified class.{wiki_link}
     *
     * @param objectId ID of the object to operate on
     * @param outputClass class to deserialize the server reponse to
     *
     * @return Response object
     *
     * @throws DXAPIException
     *             If the server returns a complete response with an HTTP status
     *             code other than 200 (OK).
     * @throws DXHTTPException
     *             If an error occurs while making the HTTP request or obtaining
     *             the response (includes HTTP protocol errors).
     */
    public static <T> T {method_name}(String objectId, Class<T> outputClass) {{
        return {method_name}(objectId, mapper.createObjectNode(), outputClass);
    }}
    /**
     * Invokes the {method_name} method with the given input, deserializing to an object of the specified class.{wiki_link}
     *
     * @param objectId ID of the object to operate on
     * @param inputObject input object (to be JSON serialized to an input hash)
     * @param outputClass class to deserialize the server reponse to
     *
     * @return Response object
     *
     * @throws DXAPIException
     *             If the server returns a complete response with an HTTP status
     *             code other than 200 (OK).
     * @throws DXHTTPException
     *             If an error occurs while making the HTTP request or obtaining
     *             the response (includes HTTP protocol errors).
     */
    public static <T> T {method_name}(String objectId, Object inputObject, Class<T> outputClass) {{
        {input_code}
        return DXJSON.safeTreeToValue(
                new DXHTTPRequest().request("/" + objectId + "/" + "{method_route}",
                        input, {retry_strategy_with_nonce}), outputClass);
    }}
    /**
     * Invokes the {method_name} method with an empty input using the given environment, deserializing to an object of the specified class.{wiki_link}
     *
     * @param objectId ID of the object to operate on
     * @param outputClass class to deserialize the server reponse to
     * @param env environment object specifying the auth token and remote server and protocol
     *
     * @return Response object
     *
     * @throws DXAPIException
     *             If the server returns a complete response with an HTTP status
     *             code other than 200 (OK).
     * @throws DXHTTPException
     *             If an error occurs while making the HTTP request or obtaining
     *             the response (includes HTTP protocol errors).
     */
    public static <T> T {method_name}(String objectId, Class<T> outputClass, DXEnvironment env) {{
        return {method_name}(objectId, mapper.createObjectNode(), outputClass, env);
    }}
    /**
     * Invokes the {method_name} method with the given input using the given environment, deserializing to an object of the specified class.{wiki_link}
     *
     * @param objectId ID of the object to operate on
     * @param inputObject input object (to be JSON serialized to an input hash)
     * @param outputClass class to deserialize the server reponse to
     * @param env environment object specifying the auth token and remote server and protocol
     *
     * @return Response object
     *
     * @throws DXAPIException
     *             If the server returns a complete response with an HTTP status
     *             code other than 200 (OK).
     * @throws DXHTTPException
     *             If an error occurs while making the HTTP request or obtaining
     *             the response (includes HTTP protocol errors).
     */
    public static <T> T {method_name}(String objectId, Object inputObject, Class<T> outputClass, DXEnvironment env) {{
        {input_code}
        return DXJSON.safeTreeToValue(
            new DXHTTPRequest(env).request("/" + objectId + "/" + "{method_route}",
                    input, {retry_strategy_with_nonce}), outputClass);
    }}

    /**
     * Invokes the {method_name} method.{wiki_link}
     *
     * @param objectId ID of the object to operate on
     *
     * @return Server response parsed from JSON
     *
     * @throws DXAPIException
     *             If the server returns a complete response with an HTTP status
     *             code other than 200 (OK).
     * @throws DXHTTPException
     *             If an error occurs while making the HTTP request or obtaining
     *             the response (includes HTTP protocol errors).
     *
     * @deprecated Use {{@link #{method_name}(String, Class)}} instead and supply your own class to deserialize to.
     */
    @Deprecated
    public static JsonNode {method_name}(String objectId) {{
        return {method_name}(objectId, mapper.createObjectNode());
    }}
    /**
     * Invokes the {method_name} method with the specified parameters.{wiki_link}
     *
     * @param objectId ID of the object to operate on
     * @param inputParams input parameters to the API call
     *
     * @return Server response parsed from JSON
     *
     * @throws DXAPIException
     *             If the server returns a complete response with an HTTP status
     *             code other than 200 (OK).
     * @throws DXHTTPException
     *             If an error occurs while making the HTTP request or obtaining
     *             the response (includes HTTP protocol errors).
     *
     * @deprecated Use {{@link #{method_name}(String, Object, Class)}} instead and supply your own class to deserialize to.
     */
    @Deprecated
    public static JsonNode {method_name}(String objectId, JsonNode inputParams) {{
        return new DXHTTPRequest().request("/" + objectId + "/" + "{method_route}", inputParams,
                {retry_strategy});
    }}
    /**
     * Invokes the {method_name} method with the specified environment.{wiki_link}
     *
     * @param objectId ID of the object to operate on
     * @param env environment object specifying the auth token and remote server and protocol
     *
     * @return Server response parsed from JSON
     *
     * @throws DXAPIException
     *             If the server returns a complete response with an HTTP status
     *             code other than 200 (OK).
     * @throws DXHTTPException
     *             If an error occurs while making the HTTP request or obtaining
     *             the response (includes HTTP protocol errors).
     *
     * @deprecated Use {{@link #{method_name}(String, Class, DXEnvironment)}} instead and supply your own class to deserialize to.
     */
    @Deprecated
    public static JsonNode {method_name}(String objectId, DXEnvironment env) {{
        return {method_name}(objectId, mapper.createObjectNode(), env);
    }}
    /**
     * Invokes the {method_name} method with the specified environment and parameters.{wiki_link}
     *
     * @param objectId ID of the object to operate on
     * @param inputParams input parameters to the API call
     * @param env environment object specifying the auth token and remote server and protocol
     *
     * @return Server response parsed from JSON
     *
     * @throws DXAPIException
     *             If the server returns a complete response with an HTTP status
     *             code other than 200 (OK).
     * @throws DXHTTPException
     *             If an error occurs while making the HTTP request or obtaining
     *             the response (includes HTTP protocol errors).
     *
     * @deprecated Use {{@link #{method_name}(String, Object, Class, DXEnvironment)}} instead and supply your own class to deserialize to.
     */
    @Deprecated
    public static JsonNode {method_name}(String objectId, JsonNode inputParams, DXEnvironment env) {{
        return new DXHTTPRequest(env).request("/" + objectId + "/" + "{method_route}", inputParams,
                {retry_strategy});
    }}'''

#app_object_method_template = '''
#def {method_name}(app_name_or_id, alias=None, input_params={{}}, **kwargs):
#    fully_qualified_version = app_name_or_id + (('/' + alias) if alias else '')
#    return DXHTTPRequest('/%s/{method_route}' % fully_qualified_version, input_params, **kwargs)
#'''
app_object_method_template = object_method_template


def make_input_code(accept_nonce):
    if accept_nonce:
        return "JsonNode input = Nonce.updateNonce(mapper.valueToTree(inputObject));"
    return "JsonNode input = mapper.valueToTree(inputObject);"

def make_retry_param(retryable):
    return "RetryStrategy.SAFE_TO_RETRY" if retryable else "RetryStrategy.UNSAFE_TO_RETRY"


print preamble

for method in json.loads(sys.stdin.read()):
    route, signature, opts = method
    method_name = signature.split("(")[0]
    wiki_link = ''
    if opts.get('wikiLink', None):
        wiki_link = '\n     *\n     * <p>For more information about this method, see the <a href="%s">API specification</a>.' % (opts['wikiLink'],)
    retryable = opts['retryable']
    accept_nonce = opts.get('acceptNonce', False)

    # retry_strategy_with_nonce and retry_strategy track whether retry
    # is permitted for overloads that supply, or don't supply, a nonce,
    # respectively. The older and deprecated overloads for each method
    # don't provide the nonce, so shouldn't be marked as retryable for
    # nonce'd routes, even if the newer overloads for the same routes
    # are marked as retryable. Compare these two overloads of the same
    # nonce'd route...
    #
    # // Supplies a nonce... is therefore retryable
    #
    # public static <T> T appRun(String objectId, Object inputObject, Class<T> outputClass) {
    #     JsonNode input = Nonce.updateNonce(mapper.valueToTree(inputObject));
    #     return DXJSON.safeTreeToValue(
    #             new DXHTTPRequest().request("/" + objectId + "/" + "run",
    #                     input, RetryStrategy.SAFE_TO_RETRY), outputClass);
    # }
    #
    # // Doesn't supply a nonce... is therefore not retryable
    #
    # @Deprecated
    # public static JsonNode appRun(String objectId, JsonNode inputParams) {
    #     return new DXHTTPRequest().request("/" + objectId + "/" + "run", inputParams,
    #             RetryStrategy.UNSAFE_TO_RETRY);
    # }

    if (opts['objectMethod']):
        root, oid_route, method_route = route.split("/")
        if oid_route == 'app-xxxx':
            print app_object_method_template.format(method_name=method_name,
                                                    method_route=method_route,
                                                    wiki_link=wiki_link,
                                                    retry_strategy_with_nonce=make_retry_param(retryable or accept_nonce),
                                                    retry_strategy=make_retry_param(retryable),
                                                    input_code=make_input_code(accept_nonce))
        else:
            print object_method_template.format(method_name=method_name,
                                                method_route=method_route,
                                                wiki_link=wiki_link,
                                                retry_strategy_with_nonce=make_retry_param(retryable or accept_nonce),
                                                retry_strategy=make_retry_param(retryable),
                                                input_code=make_input_code(accept_nonce))
    else:
        print class_method_template.format(method_name=method_name,
                                           route=route,
                                           wiki_link=wiki_link,
                                           retry_strategy_with_nonce=make_retry_param(retryable or accept_nonce),
                                           retry_strategy=make_retry_param(retryable),
                                           input_code=make_input_code(accept_nonce))

print postscript
