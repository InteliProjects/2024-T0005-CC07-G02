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
} from '@/components/ui/alert-dialog';
import { Plano } from '@/types/plano';
import { post } from '@/api/chamadasApi';
import { BaseUrlKey } from '@/api/config';

interface DialogPlanoCarouselProps {
  plano: Plano;
}

const contratarPlano = async (plano: Plano) => {
  const planoContratado = await post("/servicos_contratados_outros", {
    id_plano: plano.id,
    data_contratacao: new Date().toISOString()
  }, BaseUrlKey.LOAD_BALANCER_URL, localStorage.getItem('token') || "");

  console.log(planoContratado);
}

export default function DialogPlanoCarousel({ plano }: DialogPlanoCarouselProps) {
  return (
    <AlertDialog>
      <AlertDialogTrigger>
        <button className="bg-vivo text-white font-bold py-2 px-4 rounded-full">Saiba mais</button>
      </AlertDialogTrigger>
      <AlertDialogContent>
        <AlertDialogHeader>
          <AlertDialogTitle className="text-vivo text-3xl font-bold" >{plano.nome_do_plano}</AlertDialogTitle>
        </AlertDialogHeader>
        <AlertDialogDescription className="flex flex-col gap-6">
          <h5 className="text-lg">
            {plano.descricao}
          </h5>
          <h5 className="text-lg">
            Você tem certeza que deseja contratar esse plano?
          </h5>
        </AlertDialogDescription>
        <AlertDialogFooter>
          <AlertDialogCancel>
            Cancelar
          </AlertDialogCancel>
          <AlertDialogAction 
            className="bg-vivo"
            onClick={() => {
              contratarPlano(plano)
              console.log("Plano contratado")
            }}
          >
            Contratar
          </AlertDialogAction>
        </AlertDialogFooter>
      </AlertDialogContent>
    </AlertDialog>
  )
}