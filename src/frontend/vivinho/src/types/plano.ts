export interface Plano {
  id: string;
  nome_do_plano: string;
  descricao: string;
  valor: number;
  id_relacao?: string;
}