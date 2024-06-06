// Importa bibliotecas e módulos
import * as React from "react"
import Image from "next/image"

// Importa componentes de UI para construir cartões de conteúdo
import { 
  Card, 
  CardContent,
  CardHeader,
  CardTitle
} from "@/components/ui/card"

// Importa componentes relacionados ao carrossel, permitindo a construção de um carrossel de conteúdo navegável
import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from "@/components/ui/carousel"

// Importa imagens e o componente de diálogo para exibir detalhes do plano
import vivoLogo from "../../assets/img/Logo_VIVO.png";
import DialogPlanoCarouselOutros from "./dialogPlanoCarouselOutros";
// Importa o tipo de dados Plano
import { Plano } from "@/types/plano";
// Importa o componente de esqueleto para exibir um carregamento de conteúdo
import Skeleton from "react-loading-skeleton";

// Define a interface do componente, especificando os tipos de dados esperados
interface CarouselTvEStramingProps {
  planos: Plano[],
  carregandoPlanos: boolean
}

// Define o componente CarouselTvEStreaming, responsável por exibir um carrossel de planos de TV e Streaming.
export default function CarouselTvEStraming({ planos, carregandoPlanos }: CarouselTvEStramingProps) {
  if((planos === undefined || planos.length === 0) && carregandoPlanos === false) {
    return (
      <div>
        <h1>Não há planos disponíveis</h1>
      </div>
    )
  }
  return (
    <Carousel
      opts={{
        align: "start",
      }}
      className="w-full md:max-w-[820px] lg:max-w-7xl"
    >
      {/* Componente que contém os itens do carrossel*/}
      <CarouselContent>
        {/*Checa se os planos não estão carregando. O esqueleto é exibido enquanto os planos são carregados*/}
        {(carregandoPlanos === false) ? (
          planos.map((plano, index) => (
            //Define cada item do carrossel
            <CarouselItem key={index} className="md:basis-3/5 lg:basis-2/5">
              <div className="p-2">
                <Card className="h-[450px]">
                  <CardHeader className="flex justify-center items-center">
                    <CardTitle className="text-2xl font-bold text-vivo">
                      {plano.nome_do_plano}
                    </CardTitle>
                  </CardHeader>
                  <CardContent className="flex flex-col items-center justify-center gap-8 p-6">
                    <p className="text-center text-md">
                      {plano.descricao}
                    </p>
                    <Image 
                      src={vivoLogo}
                      alt="Imagem do Plano"
                      width={200}
                      height={200}
                    />
                    <p className="text-lg font-semibold">
                      R$ {plano.valor.toString().replace(".", ",")}/mês
                    </p>
                    <div>
                      {/*Componente para ações relacionadas ao plano */}
                      <DialogPlanoCarouselOutros plano={plano} />
                    </div>
                  </CardContent>
                </Card>
              </div>
            </CarouselItem>
          ))) : (
          Array.from({ length: 4 }).map((_, index) => (
            //Define os itens para o esqueleto que serão exibidos enquanto os planos são carregados
            <CarouselItem key={index} className="md:basis-3/5 lg:basis-2/5">
              <div className="p-2">
                <Card className="h-[450px]">
                  <CardHeader className="flex justify-center items-center">
                    <CardTitle>
                      <Skeleton width={150} height={30} />
                    </CardTitle>
                  </CardHeader>
                  <CardContent className="flex flex-col items-center justify-center gap-8 p-6">
                    <p>
                      <Skeleton width={150} count={2} />
                    </p>
                      <Skeleton width={200} height={100}/>
                    <p className="text-lg font-semibold">
                      <Skeleton />
                    </p>
                    <div>
                      <Skeleton width={150} height={40} />
                    </div>
                  </CardContent>
                </Card>
              </div>
            </CarouselItem>
          ))
        )}
      </CarouselContent>
      {/* Botões de navegação do carrossel */	}
      <CarouselPrevious />
      <CarouselNext />
      {/* Fim do componente CarouselTvEStreaming */}
    </Carousel>
  )
}
