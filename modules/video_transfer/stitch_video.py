# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import sys
import os
import subprocess
from azureml.pipeline.wrapper import dsl
from azureml.pipeline.wrapper.dsl.module import ModuleExecutor, InputDirectory, OutputDirectory


@dsl.module(
    description='stitch images and audio back to video',
    name='stitch video',
)
def stitch_video(
    input_images: InputDirectory(description="input directory of images"),
    input_audio: InputDirectory(description="input directory of audio"),
    output_video: OutputDirectory(description="output directory of stitched video file")
):

## this module takes input video, and slice the video into images with ffmpeg   

    subprocess.run("ffmpeg -framerate 30 -i {}/%05d_video.jpg -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p "
               "-y {}/video_without_audio.mp4"
               .format(args.images_dir, args.output_dir),
               shell=True, check=True)

    subprocess.run("ffmpeg -i {}/video_without_audio.mp4 -i {}/video.aac -map 0:0 -map 1:0 -vcodec "
               "copy -acodec copy -y {}/video_with_audio.mp4"
               .format(args.output_dir, args.input_audio, args.output_dir),
               shell=True, check=True)



if __name__ == '__main__':
    ModuleExecutor(stitch_video).execute(sys.argv)
