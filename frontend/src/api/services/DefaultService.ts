/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { PatchRequest } from '../models/PatchRequest';
import type { PatchResponse } from '../models/PatchResponse';
import type { Response } from '../models/Response';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class DefaultService {

    /**
     * Retrieves a list of craftsmen based on postal code
     * @param postalcode Postal code to filter craftsmen
     * @param below Only return the results with a score blow this value
     * @returns Response List of craftsmen
     * @throws ApiError
     */
    public static getCraftsmen(
        postalcode: string,
        below?: number,
    ): CancelablePromise<Response> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/craftsmen',
            query: {
                'postalcode': postalcode,
                'below': below,
            },
        });
    }

    /**
     * Updates a craftsman's profile information
     * @param craftmanId Unique ID of the craftsman
     * @param requestBody
     * @returns PatchResponse Craftsman updated successfully
     * @throws ApiError
     */
    public static patchCraftman(
        craftmanId: number,
        requestBody: PatchRequest,
    ): CancelablePromise<PatchResponse> {
        return __request(OpenAPI, {
            method: 'PATCH',
            url: '/craftman/{craftman_id}',
            path: {
                'craftman_id': craftmanId,
            },
            body: requestBody,
            mediaType: 'application/json',
        });
    }

}
