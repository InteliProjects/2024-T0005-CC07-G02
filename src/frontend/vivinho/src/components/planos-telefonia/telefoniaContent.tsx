// Indica o uso em um ambiente do cliente em vez de um servidor.
"use client";

// Importa os hooks do React, useEffect e useState
import { useEffect, useState } from "react";
// Importa a função v4 do pacote uuid
import { v4 as uuidv4 } from "uuid";
// Importa o tipo Plano do arquivo plano.ts
import { Plano } from "@/types/plano";
// Importa os componentes CardPlanosTelefonia e CarrosselTelefonia
import CardPlanosTelefonia from "./cardPlanoTelefonia";
import CarrosselTelefonia from "./carrosselTelefonia";
// Importa a função get para fazer requisições GET
import { get } from "@/api/chamadasApi";
// Importa chave de configuração BaseUrlKey
import { BaseUrlKey } from "@/api/config";
// Importa tipagem Response
import { Response } from "@/types/response";

// Define a interface PlanoContratado com suas propriedades
interface PlanoContratado {
  data_cancelamento: string | null;
  data_contratacao: string;
  id: string;
  id_cliente: string;
  id_plano: string;
}

// Define a função getPlanosContratados que retorna um array de planos contratados
const getPlanosContratados = async () => {
  const planos = await get<Response>("/servicos_contratados_telefonia", BaseUrlKey.LOAD_BALANCER_URL, localStorage.getItem('token') || "");

  const planosContratados = planos.data;

  console.log(planosContratados);
  return planosContratados;
}

// Define a função getAllPlans que retorna um array de planos
const getAllPlans = async () => {
  const planos = await get<Response>("/planos_telefonia", BaseUrlKey.LOAD_BALANCER_URL, localStorage.getItem('token') || "");

  return planos.data;
}

// Define a função TelefoniaContent, componente principal para conteúdo de telefonia
export default function TelefoniaContent() {
  //Define estados para planos contratados, planos disponíveis e estados de carregamento
  const [planosContratados, setPlanosContratados] = useState<Plano[]>([]);
  const [planos, setPlanos] = useState<Plano[]>([]);
  const [carregandoPlanosContratados, setCarregandoPlanosContratados] = useState(true);
  const [carregandoPlanos, setCarregandoPlanos] = useState(true);
  
  // Define o useEffect para buscar os planos contratados e disponíveis
  useEffect(() => {
    const fetchPlanos = async () => {
      try {
        // Busca os planos disponíveis
        const planos = await getAllPlans();
        setPlanos(planos.data);
        setCarregandoPlanos(false);

        // Busca os planos contratados e filtra os planos disponíveis
        const planosContratados = await getPlanosContratados();
        const planosFiltrados = planosContratados.data.filter((planoContratado: PlanoContratado) => {
          return planos.data.some((plano: Plano) => planoContratado.id_plano === plano.id);
        });
        
        // Adiciona a propriedade id_relacao aos planos contratados
        const planosFiltradosComExtra = planosFiltrados.map((planoContratado: PlanoContratado) => {
          const planoCorrespondente = planos.data.find((plano: Plano) => planoContratado.id_plano === plano.id);
          return {
            ...planoCorrespondente,
            id_relacao: planoContratado.id,
          };
        });

        setPlanosContratados(planosFiltradosComExtra);
        setCarregandoPlanosContratados(false);
        console.log(planosFiltradosComExtra);
      } catch (error) {
        console.error(error);
        setCarregandoPlanos(false);
      }
    };
    fetchPlanos();
  }, []);

  // Renderiza o componente, passando os planos contratados e disponíveis e os estados de carregamento
	return (
		<>
			<h1 className="text-1xl font-semibold tracking-tight text-vivo p-2">
				Planos de Telefonia Contratados:
			</h1>
			<CardPlanosTelefonia planosContratados={planosContratados} carregandoPlanosContratados={carregandoPlanosContratados} />
			<h2 className="text-1xl font-semibold tracking-tight text-vivo p-2">
				Outros Planos para contratar:
			</h2>
			<div className="flex justify-center items-center">
				<CarrosselTelefonia planos={planos} carregandoPlanos={carregandoPlanos} />
			</div>
		</>
	);
}
