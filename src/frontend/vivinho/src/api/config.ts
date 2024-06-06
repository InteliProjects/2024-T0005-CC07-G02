import axios, { AxiosInstance } from 'axios';

export enum BaseUrlKey {
  USUARIO_API = 'REACT_APP_API_USUARIO_URL',
  FATURA_API = 'REACT_APP_API_FATURA_URL',
  INTERNET_API = 'REACT_APP_API_INTERNET_URL',
  TELEFONIA_API = 'REACT_APP_API_TELEFONIA_URL',
  TV_E_STREAMING_API = 'REACT_APP_API_TV_E_STREAMING_URL',
  LOAD_BALANCER_URL = 'LOAD_BALANCER_URL',
  LOAD_BALANCER_URL_CADASTRO = "LOAD_BALANCER_URL_CADASTRO"
}

// Mapeamento das chaves do enum para as URLs
const baseUrls: Record<BaseUrlKey, string | undefined> = {
  [BaseUrlKey.USUARIO_API]: process.env.REACT_APP_API_USUARIO_URL,
  [BaseUrlKey.FATURA_API]: process.env.REACT_APP_API_FATURA_URL,
  [BaseUrlKey.INTERNET_API]: process.env.REACT_APP_API_INTERNET_URL,
  [BaseUrlKey.TELEFONIA_API]: process.env.REACT_APP_API_TELEFONIA_URL,
  [BaseUrlKey.TV_E_STREAMING_API]: process.env.REACT_APP_API_TV_E_STREAMING_URL || "http://localhost:3003/outros_servicos/api",
  [BaseUrlKey.LOAD_BALANCER_URL]: process.env.LOAD_BALANCER_URL || "http://ec2-44-218-58-178.compute-1.amazonaws.com",
  [BaseUrlKey.LOAD_BALANCER_URL_CADASTRO]: process.env.LOAD_BALANCER_URL_CADASTRO || "http://ec2-44-218-58-178.compute-1.amazonaws.com:85"
};


export function axiosComBaseUrl(baseUrlKey: keyof typeof baseUrls): AxiosInstance {
  const baseUrl = baseUrls[baseUrlKey];
  console.log(`Base URL para a chave ${baseUrlKey}: ${baseUrl}`);
  if (!baseUrls[baseUrlKey]) {
    throw new Error(`Base URL não encontrada para a chave ${baseUrlKey}`);
  }

  return axios.create({
    baseURL: baseUrl as string,
  });
}