import { useState, useCallback } from 'react';
import client from '@/lib/apiClient';
import type { ApiResponse } from '@/types';

interface UseApiState<T> {
  data: T | null;
  loading: boolean;
  error: string | null;
}

export function useApi<T = unknown>() {
  const [state, setState] = useState<UseApiState<T>>({
    data: null,
    loading: false,
    error: null,
  });

  const request = useCallback(
    async (
      method: 'GET' | 'POST' | 'PUT' | 'DELETE',
      url: string,
      data?: unknown
    ) => {
      setState({ data: null, loading: true, error: null });

      try {
        const response = await client({
          method,
          url,
          data,
        });

        setState({
          data: response as T,
          loading: false,
          error: null,
        });

        return response;
      } catch (err) {
        const error = err instanceof Error ? err.message : 'Unknown error';
        setState({
          data: null,
          loading: false,
          error,
        });
        throw err;
      }
    },
    []
  );

  return {
    ...state,
    get: (url: string) => request('GET', url),
    post: (url: string, data: unknown) => request('POST', url, data),
    put: (url: string, data: unknown) => request('PUT', url, data),
    delete: (url: string) => request('DELETE', url),
  };
}
