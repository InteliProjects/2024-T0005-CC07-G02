"use client";
// Importa componentes específicos de UI para avatar, botão, card, e tabs da estrutura de diretórios local.
// Importa o componente Image do Next.js para otimização de imagens.
import vivoLogo from "@/assets/img/Logo_VIVO.png";
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

import {
  Tabs,
  TabsContent,
  TabsList,
  TabsTrigger
} from "@/components/ui/tabs"

// Importa componentes específicos de funcionalidades e layout da aplicação.
import Image from "next/image";
import { Overview } from "@/components/overview/overview";
import { UserNav } from "@/components/user-nav/userNav";
import TvEStreamingContent from "@/components/planos-tv-e-straming/tvEStreamingContent";
import TelefoniaContent from "@/components/planos-telefonia/telefoniaContent";
import InternetContent from "@/components/planos-internet/internetContent";
import { Plano } from "@/types/plano";
import { useState, useEffect } from "react";
import { BaseUrlKey } from "@/api/config";
import { get } from "@/api/chamadasApi";
import { Response } from "@/types/response";

interface PlanoContratadoOutros {
  data_cancelamento: string | null;
  data_contratacao: string;
  id: string;
  id_cliente: string;
  id_plano: string;
}

// Funções assíncronas para obter dados de planos contratados e disponíveis de diferentes serviços (Outros, Internet, Telefonia).
const getPlanosContratados = async () => {
  const planos = await get<Response>("/servicos_contratados_outros", BaseUrlKey.LOAD_BALANCER_URL, localStorage.getItem('token') || "");

  const planosContratados = planos.data;

  return planosContratados;
}

const getAllPlans = async () => {
  const planos = await get<Response>("/planos_outros", BaseUrlKey.LOAD_BALANCER_URL, localStorage.getItem('token') || "");

  return planos.data;
}

const getPlanosContratadosInternet = async () => {
  const planos = await get<Response>("/servicos_contratados_internet", BaseUrlKey.LOAD_BALANCER_URL, localStorage.getItem('token') || "");

  const planosContratados = planos.data;

  return planosContratados;
}

const getAllPlansInternet = async () => {
  const planos = await get<Response>("/planos_internet", BaseUrlKey.LOAD_BALANCER_URL, localStorage.getItem('token') || "");

  return planos.data;
}

const getPlanosTelefonia = async () => {
  const planos = await get<Response>("/planos_telefonia", BaseUrlKey.LOAD_BALANCER_URL, localStorage.getItem('token') || "");

  return planos.data;
}

const getPlanosContratadosTelefonia = async () => {
  const planos = await get<Response>("/servicos_contratados_telefonia", BaseUrlKey.LOAD_BALANCER_URL, localStorage.getItem('token') || "");

  const planosContratados = planos.data;

  return planosContratados;
}

// Componente principal Dashboard, que gerencia o estado e renderiza a UI do dashboard do usuário.
export default function Dashboard() {
  // Estados para armazenar valores calculados e quantidade de planos por categoria.
  const [valorOutrosServicos, setValorOutrosServicos] = useState(0);
  const [valorInternet, setValorInternet] = useState(0);
  const [valorTelefonia, setValorTelefonia] = useState(0);

  const [qntdPlanosInternet, setQntdPlanosInternet] = useState(0);
  const [qntdPlanosOutros, setQntdPlanosOutros] = useState(0);
  const [qntdPlanosTelefonia, setQntdPlanosTelefonia] = useState(0);

  useEffect(() => {
     // Função assíncrona para buscar dados de planos e calcular valores totais e quantidades.
    const fetchPlanos = async () => {
      try {
        const planos = await getAllPlans();
        const planosContratados = await getPlanosContratados();
        const planosFiltrados = planosContratados.data.filter((planoContratado: PlanoContratadoOutros) => {
          return planos.data.some((plano: Plano) => planoContratado.id_plano === plano.id);
        });

        const planosFiltradosComExtra = planosFiltrados.map((planoContratado: PlanoContratadoOutros) => {
          
          const planoCorrespondente = planos.data.find((plano: Plano) => planoContratado.id_plano === plano.id);
          return {
            ...planoCorrespondente,
            id_relacao: planoContratado.id,
          };
        });
        console.log("oie", planosFiltradosComExtra);
        
        setQntdPlanosOutros(planosFiltradosComExtra.length);
        let valorTotal = 0;
        planosFiltradosComExtra.forEach((plano: any) => {
          valorTotal += parseFloat(plano.valor);
        });
        console.log("total", valorTotal);
        setValorOutrosServicos(valorTotal);

        const planosInternet = await getAllPlansInternet();
        const planosContratadosInternet = await getPlanosContratadosInternet();
        const planosFiltradosInternet = planosContratadosInternet.data.filter((planoContratado: PlanoContratadoOutros) => {
          return planosInternet.data.some((plano: Plano) => planoContratado.id_plano === plano.id);
        });

        const planosFiltradosComExtraInternet = planosFiltradosInternet.map((planoContratado: PlanoContratadoOutros) => {
          
          const planoCorrespondente = planosInternet.data.find((plano: Plano) => planoContratado.id_plano === plano.id);
          return {
            ...planoCorrespondente,
            id_relacao: planoContratado.id,
          };
        });

        setQntdPlanosInternet(planosFiltradosComExtraInternet.length);
        let valorTotalInternet = 0;
        planosFiltradosComExtraInternet.forEach((plano: any) => {
          valorTotalInternet += parseFloat(plano.valor);
        });
        setValorInternet(valorTotalInternet);

        const planosTelefonia = await getPlanosTelefonia();
        const planosContratadosTelefonia = await getPlanosContratadosTelefonia();
        const planosFiltradosTelefonia = planosContratadosTelefonia.data.filter((planoContratado: PlanoContratadoOutros) => {
          return planosTelefonia.data.some((plano: Plano) => planoContratado.id_plano === plano.id);
        });

        const planosFiltradosComExtraTelefonia = planosFiltradosTelefonia.map((planoContratado: PlanoContratadoOutros) => {
          
          const planoCorrespondente = planosTelefonia.data.find((plano: Plano) => planoContratado.id_plano === plano.id);
          return {
            ...planoCorrespondente,
            id_relacao: planoContratado.id,
          };
        });

        setQntdPlanosTelefonia(planosFiltradosComExtraTelefonia.length);
        let valorTotalTelefonia = 0;
        planosFiltradosComExtraTelefonia.forEach((plano: any) => {
          valorTotalTelefonia += parseFloat(plano.valor);
        });
        setValorTelefonia(valorTotalTelefonia);

      } catch (error) {
        console.error(error);
      }
    };
    fetchPlanos();
  }, []);
  
  return (
    // Renderiza a estrutura principal do dashboard com componentes de UI personalizados.
    // Inclui abas para diferentes categorias de serviços e resumo de fatura.
    <>
      <div className="flex-col md:flex">
        <div className="border-b">
          <div className="flex h-16 items-center px-2 sm:px-4">
            <div className="p-2 w-full flex items-center justify-between space-x-2 sm:space-x-4">
              <Image src={vivoLogo} alt="Vivo" height={30} />
              <UserNav />
            </div>
          </div>
        </div>
        <div className="space-y-2 p-2 sm:p-4 md:p-8 pt-2 sm:pt-4 md:pt-6">
        <div className="flex items-center justify-center sm:justify-between space-y-2">
          <h2 className="sm:text-center text-2xl sm:text-3xl font-bold tracking-tight text-vivo">Dashboard</h2>
          </div>
          <Tabs defaultValue="overview" className="space-y-2 sm:space-y-4">
            <TabsList>
              <TabsTrigger value="overview">Resumo</TabsTrigger>
              <TabsTrigger value="internet">
                Internet
              </TabsTrigger>
              <TabsTrigger value="telefonia">
                Telefonia
              </TabsTrigger>
              <TabsTrigger value="tvEstreaming">
                TV e Streaming
              </TabsTrigger>
            </TabsList>
            <TabsContent value="overview" className="space-y-2 sm:space-y-4">
              <div className="flex flex-col sm:flex-row w-full justify-between gap-x-2 sm:gap-x-4">
                <Card className="flex-auto">
                  <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                    <CardTitle className="text-sm font-medium">
                      Internet
                    </CardTitle>
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      className="h-4 w-4 text-muted-foreground"
                    >
                      <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6" />
                    </svg>
                  </CardHeader>
                  <CardContent>
                    <div className="text-2xl font-bold text-vivo">R$ {valorInternet.toString().replace(".", ",")}/mês</div>
                    <p className="text-xs text-muted-foreground">
                      {qntdPlanosInternet <= 1 ? `${qntdPlanosInternet} Plano`: `${qntdPlanosInternet} Planos`}
                    </p>
                  </CardContent>
                </Card>
                <Card className="flex-auto">
                  <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                    <CardTitle className="text-sm font-medium">
                      Telefonia
                    </CardTitle>
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      className="h-4 w-4 text-muted-foreground"
                    >
                      <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2" />
                      <circle cx="9" cy="7" r="4" />
                      <path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75" />
                    </svg>
                  </CardHeader>
                  <CardContent>
                    <div className="text-2xl font-bold text-vivo">R${valorTelefonia.toString().replace(".", ",")}/mês</div>
                    <p className="text-xs text-muted-foreground">
                      {qntdPlanosTelefonia <= 1 ? `${qntdPlanosTelefonia} Plano`: `${qntdPlanosTelefonia} Planos`}
                    </p>
                  </CardContent>
                </Card>
                <Card className="flex-auto">
                  <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                    <CardTitle className="text-sm font-medium">TV e Streaming</CardTitle>
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      className="h-4 w-4 text-muted-foreground"
                    >
                      <rect width="20" height="14" x="2" y="5" rx="2" />
                      <path d="M2 10h20" />
                    </svg>
                  </CardHeader>
                  <CardContent>
                    <div className="text-2xl font-bold text-vivo">R$ {valorOutrosServicos.toString().replace(".", ",")}/mês</div>
                    <p className="text-xs text-muted-foreground">
                      {qntdPlanosOutros <= 1 ? `${qntdPlanosOutros} Plano`: `${qntdPlanosOutros} Planos`}
                    </p>
                  </CardContent>
                </Card>
                <Card className="flex-auto">
                  <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                    <CardTitle className="text-sm font-medium">
                      Fatura
                    </CardTitle>
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      className="h-4 w-4 text-muted-foreground"
                    >
                      <path d="M22 12h-4l-3 9L9 3l-3 9H2" />
                    </svg>
                  </CardHeader>
                  <CardContent>
                    <div className="text-2xl font-bold text-vivo">R$ {(valorOutrosServicos+valorInternet+valorTelefonia).toString().replace(".", ",")}</div>
                    <p className="text-xs text-muted-foreground">
                      Vencimento: 10/03/2024
                    </p>
                  </CardContent>
                </Card>
              </div>
              <div className="grid gap-2 sm:gap-4 md:grid-cols-2 lg:grid-cols-7">
                <Card className="col-span-4">
                  <CardHeader>
                    <CardTitle>Overview</CardTitle>
                  </CardHeader>
                  <CardContent className="pl-2">
                    <Overview />
                  </CardContent>
                </Card>
                <Card className="col-span-3 max-sm:col-span-4">
                  <CardHeader>
                    <CardTitle>Resumo da fatura</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="divide-y divide-gray-200">
                      <div className="flex justify-between py-2">
                        <span className="font-bold text-gray-800">Serviço</span>
                        <span className="font-bold text-gray-800">Valor</span>
                      </div>
                      {/* Itens da fatura */}
                      <div className="flex justify-between py-4">
                        <span className="font-medium text-gray-600">Telefonia</span>
                        <span className="font-semibold text-gray-800">R$ {valorTelefonia}</span>
                      </div>
                      <div className="flex justify-between py-4">
                        <span className="font-medium text-gray-600">Internet</span>
                        <span className="font-semibold text-gray-800">R$ {valorInternet}</span>
                      </div>
                      <div className="flex justify-between py-4">
                        <span className="font-medium text-gray-600">TV e Streaming</span>
                        <span className="font-semibold text-gray-800">R$ {valorOutrosServicos}</span>
                      </div>
                      <div className="flex justify-between py-4">
                        <span className="font-medium text-gray-600"><strong>Total</strong></span>
                        <span className="font-semibold text-gray-800"><strong>R$ {(valorOutrosServicos+valorInternet+valorTelefonia).toString().replace(".", ",")}</strong></span>
                      </div>
                    </div>
                  </CardContent>
                </Card>

              </div>
            </TabsContent>
            <TabsContent value="internet" className="space-y-4">
              <InternetContent />
            </TabsContent>

            <TabsContent value="telefonia" className="space-y-4">
              <TelefoniaContent />
            </TabsContent>

            <TabsContent value="tvEstreaming" className="space-y-4">
              <TvEStreamingContent />
            </TabsContent>
          </Tabs>
        </div>
      </div>
    </>
  );
}
