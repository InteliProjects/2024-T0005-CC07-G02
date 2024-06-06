import {
	AlertDialog,
	AlertDialogAction,
	AlertDialogCancel,
	AlertDialogContent,
	AlertDialogDescription,
	AlertDialogFooter,
	AlertDialogHeader,
	AlertDialogTitle,
	AlertDialogTrigger,
} from "@/components/ui/alert-dialog";

import { MdCancel } from "react-icons/md";
import { Plano } from "@/types/plano";
import { BaseUrlKey } from "@/api/config";
import { del } from "@/api/chamadasApi";
interface DialogAcoesCarouselProps {
  plano: Plano;
}

const deletarPlanoContratado = async (plano: Plano) => {
  const planos = await del<Response>(`/servicos_contratados_outros/${plano.id_relacao}`, BaseUrlKey.LOAD_BALANCER_URL, localStorage.getItem('token') || "");

  const planosContratados = planos.data;

  console.log(planosContratados);
  return planosContratados;
}

export default function DialogAcoesCarousel({plano}: DialogAcoesCarouselProps) {
	return (
		<div className="flex gap-4">
			<AlertDialog>
				<AlertDialogTrigger className="flex justify-center items-center">
          <MdCancel className="text-vivo font-light py-2 px-4 h-16 w-20 rounded-full"/>
				</AlertDialogTrigger>
				<AlertDialogContent>
					<AlertDialogHeader>
						<AlertDialogTitle className="text-vivo text-3xl font-bold">{plano.nome_do_plano}</AlertDialogTitle>
					</AlertDialogHeader>
					<AlertDialogDescription className="flex flex-col gap-6">
            <h5 className="text-lg">
						  {plano.descricao}
            </h5>
            <h5 className="text-lg">
              Você tem certeza que deseja cancelar este plano?
            </h5>
					</AlertDialogDescription>
					<AlertDialogFooter>
						<AlertDialogCancel>Não</AlertDialogCancel>
						<AlertDialogAction className="bg-vivo"
							onClick={() => {
								deletarPlanoContratado(plano);
								console.log("Plano cancelado com sucesso");
							}}
						>Sim</AlertDialogAction>
					</AlertDialogFooter>
				</AlertDialogContent>
			</AlertDialog>
		</div>
	);
}
