// Indica o uso em um ambiente do cliente em vez de um servidor
"use client"

// Importa a biblioteca React Loading Skeleton para mostrar placeholders de carregamento
import Skeleton from 'react-loading-skeleton'
import 'react-loading-skeleton/dist/skeleton.css'
// Importa os componentes de card e dialog de ações de telefonia
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import DialogAcoesTelefonia from "@/components/planos-telefonia/dialogAcoesTelefonia";
// Importa o tipo (interface) Plano, para tipagem dos planos de telefonia.
import { Plano } from "@/types/plano";
// Importa a biblioteca React para a criação de componentes
import React from 'react';

// Define as propriedades do componente CardPlanosTelefonia
interface CardPlanosTelefoniaProps {
    planosContratados: Plano[];
		carregandoPlanosContratados: boolean;
}

// Componente funcional CardPlanosTelefonia que aceita as propriedades definidas acima 
export default function CardPlanosTelefonia({ planosContratados, carregandoPlanosContratados }: CardPlanosTelefoniaProps)  {
    return (
        // Cria uma grade para organizar os cartões dos planos
        <div className="grid gap-4 md:grid-cols-4 lg:grid-cols-4 sm:grid-cols-4">
            {(carregandoPlanosContratados === false) ? (
                // Se os dados não estiverem carregando, mapeia os planosContratados para mostrar os cartões dos planos
                planosContratados.map((plano, index) => (
                     // Usa React.Fragment para agrupar vários elementos filhos sem adicionar nós extras ao DOM
                    <React.Fragment key={plano.id_relacao}>
                        {/*Cria um cartão para mostrar o tipo do plano e define o cabeçalho e o conteúdo do cartão*/}
                        <Card className="flex flex-col justify-center">
                            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                <CardTitle className="text-sm font-medium flex w-full justify-between">
                                    <h1>Tipo do Plano</h1>
                                    <p>Plano {index + 1}</p>
                                </CardTitle>
                            </CardHeader>
                            <CardContent>
                                {/* Exibe o nome do plano */}
                                <div className="text-2xl font-bold text-vivo">
                                    {plano.nome_do_plano}
                                </div>
                            </CardContent>
                        </Card>
                         {/* Cria um segundo cartão para mostrar a descrição do plano */}
                        <Card className="flex flex-col justify-center">
                            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                {/* Exibe a descrição do plano */}
                                <CardTitle className="text-sm font-medium">
                                    Descrição do Plano
                                </CardTitle>
                            </CardHeader>
                            <CardContent>
                                <div className="text-2xl font-bold text-vivo">
                                    {plano.descricao}
                                </div>
                            </CardContent>
                        </Card>
                        {/* Cria um terceiro cartão para mostrar o valor do plano */}
                        <Card className="flex flex-col justify-center">
                            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                <CardTitle className="text-sm font-medium">
                                    Valor do Plano
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
                                <div className="text-2xl font-bold text-vivo">
                            {/* Exibe o valor do plano, formatando o número para exibir uma vírgula como separador decimal */}
                                    R$ {plano.valor.toString().replace(".", ",")}/mês
                                </div>
                            </CardContent>
                        </Card>
                        {/* Cria um quarto cartão para ações relacionadas ao plano */}
                        <Card className="flex flex-col justify-center w-1/2 md:w-full">
                            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                <CardTitle className="text-sm font-medium">
                                    Ações
                                </CardTitle>
                            </CardHeader>
                            {/* Exibe componentes de ação para o plano */}
                            <CardContent>
                                <div className="font-bold text-vivo flex justify-center items-center">
                                    <DialogAcoesTelefonia plano={plano} />
                                </div>
                            </CardContent>
                        </Card>
                    </React.Fragment>
                ))
            ) : (
                  // Enquanto os dados estiverem carregando, exibe cartões com esqueletos de carregamento
                Array.from({ length: 1 }).map((_, index) => (
                    <React.Fragment key={index}>
                        {/* Inicia um grupo de cartões (Cards) para representar visualmente o esqueleto de cada parte do plano enquanto está sendo carregado */}
                        <Card className="flex flex-col justify-center">
                            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                <CardTitle className="text-sm font-medium flex w-full justify-between">
                                    <h1><Skeleton  count={1} width={60} height={20} /></h1>
                                    <p><Skeleton /></p>
                                </CardTitle>
                            </CardHeader>
                            <CardContent>
                                <div className="text-2xl font-bold text-vivo">
                                    <Skeleton />
                                </div>
                            </CardContent>
                        </Card>
                        <Card className="flex flex-col justify-center">
                            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                <CardTitle className="text-sm font-medium">
                                    <Skeleton  count={1} width={60} height={20} />
                                </CardTitle>
                            </CardHeader>
                            <CardContent>
                                <div className="text-2xl font-bold text-vivo">
                                    <Skeleton />
                                </div>
                            </CardContent>
                        </Card>
                        <Card className="flex flex-col justify-center">
                            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                <CardTitle className="text-sm font-medium">
                                    <Skeleton  count={1} width={60} height={20} />
                                </CardTitle>
                            </CardHeader>
                            <CardContent>
                                <div className="text-2xl font-bold text-vivo">
                                    <Skeleton />
                                </div>
                            </CardContent>
                        </Card>
                        <Card className="flex flex-col justify-center w-1/2 md:w-full">
                            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                <CardTitle className="text-sm font-medium">
                                    <Skeleton  count={1} width={60} height={20} />
                                </CardTitle>
                            </CardHeader>
                            <CardContent>
                                <div className="font-bold text-vivo flex justify-center items-center">
                                    <Skeleton width={50} height={50} circle />
                                </div>
                            </CardContent>
                        </Card>
                    </React.Fragment>
                ))
            )}
        </div>
    );
}
