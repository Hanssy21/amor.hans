import api from '../api/axios';

export const enviarPulso = async (data) => {
  const response = await api.post('/api/pulso/', data);
  return response.data;
};
