import os
from moviepy.editor import VideoFileClip

def convert_to_format(input_file, output_format):
    # Obtener el nombre del archivo sin la extensión
    file_name, _ = os.path.splitext(input_file)
    
    # Definir el nombre del archivo de salida con la extensión correspondiente al formato deseado
    output_file = f"{file_name}.{output_format}"

    try:
        # Cargar el archivo de video
        clip = VideoFileClip(input_file)
        
        # Verifica el formato de salida y convierte
        if output_format == 'mp4':
            clip.write_videofile(output_file, codec='libx264', preset='medium', audio_codec='aac', bitrate=None)
        elif output_format == 'avi':
            clip.write_videofile(output_file, codec='mpeg4', bitrate=None)
        elif output_format == 'webm':
            clip.write_videofile(output_file, codec='libvpx', audio_codec='libvorbis', bitrate=None)
        elif output_format == 'mkv':
            clip.write_videofile(output_file, codec='libx264', audio_codec='aac', bitrate=None)  # Puedes usar 'libvorbis' también para audio

        print(f"Conversión exitosa: {input_file} -> {output_file}")
    except Exception as e:
        print(f"Error al convertir {input_file}: {e}")

def main():
    # Obtener la lista de archivos en el directorio actual
    files = [f for f in os.listdir() if f.endswith(('.mp4', '.avi', '.webm', '.mkv'))]

    # Formato de salida deseado: 'mp4', 'avi', 'webm' o 'mkv'
    output_format = 'mp4'  # Cambiar a 'mp4', 'avi', 'webm' o 'mkv' según el formato deseado

    # Procesar cada archivo de video y convertirlo al formato especificado
    for video_file in files:
        convert_to_format(video_file, output_format)

if __name__ == "__main__":
    main()