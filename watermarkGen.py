import argparse
from pathlib import Path
import os
from func import func


parser = argparse.ArgumentParser("Adicionar Watermarks da igreja")
parser.add_argument("dir", 
                    help="Diretorio base onde contem as fotos",
                    type=Path,
                    )

parser.add_argument("-o", "--output",
                    default=None,
                    type=Path,
                    help="Diretorio de output, default=Criação de um dir 'out'",
                    dest="output")

parser.add_argument("-w", "--watermark",
                    default=None,
                    type=Path,
                    help="Marca da agua a ser adicionada, default=Marca da agua IEBA",
                    dest="watermark")

args = parser.parse_args()

dir = Path(args.dir)

if (not os.path.exists(args.dir)):
    print("Diretorio base das fotos inexistente")
    exit()

if(not args.output):
    args.output = f"{args.dir}/out/"


if (not os.path.exists(args.output)):
    print("Criando diretorio")
    os.mkdir(args.output)
else:
    print("Diretorio existe")

if (not args.watermark):
    print("Usando marca da agua default")
    temp = os.path.dirname(os.path.realpath(__file__))
    args.watermark = f"{temp}/watermark.png"


if (not os.path.isfile(args.watermark)):
    print("Marca da água inexistente ou indisponivel")
    raise SystemExit
else:
    ext = os.path.splitext(args.watermark)[1]
    if(ext!=".png"):
        print("No momento marcas de aguas aceitas são somente em formato png")
        raise SystemExit

print("Starting")

func(args.dir, args.watermark, args.output)

print("Done")