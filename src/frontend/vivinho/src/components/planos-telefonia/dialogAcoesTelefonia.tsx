// Importa os componentes necessários para a criação do diálogo de ações de telefonia
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

// Importa o ícone de cancelamento
import { MdCancel } from "react-icons/md";
// Importa a tipagem Plano para definir o tipo de dados esperado
import { Plano } from "@/types/plano";
// Importa a chave de URL base
import { BaseUrlKey } from "@/api/config";
// Importa o tipo de resposta da API
import { del } from "@/api/chamadasApi";

// Define a interface do componente, especificando os tipos de dados esperados
interface DialogAcoesTelefoniaProps {
  plano: Plano;
}

// Define a função assíncrona deletarPlanoContratado
const deletarPlanoContratado = async (plano: Plano) => {
  // Faz a chamada à API para deletar o plano contratado, passando o id do plano 
  const planos = await del<Response>(`/servicos_contratados_telefonia/${plano.id_relacao}`, BaseUrlKey.LOAD_BALANCER_URL, localStorage.getItem('token') || "");

// Extrai os dados da resposta da API
  const planosContratados = planos.data;

  console.log(planosContratados);
  // Retorna os planos contratados
  return planosContratados;
}

// Define o componente DialogAcoesTelefonia, que é responsável por exibir um diálogo de ações de telefonia
export default function DialogAcoesTelefonia({plano}: DialogAcoesTelefoniaProps) {
	return (
		//Cria uma div responsavel por alinhar os elementos
		<div className="flex gap-4">
			<AlertDialog>
				{ /* Botão para abrir o AlertDialog, usando um ícone de cancelamento. */}
				<AlertDialogTrigger className="flex justify-center items-center">
          <MdCancel className="text-vivo font-light py-2 px-4 h-16 w-20 rounded-full"/>
				</AlertDialogTrigger>
				{ /* Conteúdo do AlertDialog */}
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
						{ /* Botões de ação do AlertDialog */}
						<AlertDialogCancel>Não</AlertDialogCancel>
						<AlertDialogAction className="bg-vivo"
							onClick={() => {
								{ /* Função deletarPlanoContratado é executada ao clicar no botão "Sim" */}
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
