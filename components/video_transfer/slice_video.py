# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import sys
import os
import subprocess
from azureml.pipeline.wrapper import dsl
from azureml.pipeline.wrapper.dsl.component import componentExecutor, InputDirectory, OutputDirectory


@dsl.component(
    description='slice input video into images and audio',
    name='slice video',
)
def slice_video(
    input_video: InputDirectory(description="input directory of video file") = './data/input/video',
    output_audio: OutputDirectory(description="output directory of audio from video") = '/data/output/video',
    output_images: OutputDirectory(description="output directory of images slice from video") = '/data/output/images',
):

## this component takes input video, and slice the video into images with ffmpeg   

    subprocess.run("ffmpeg -i {} {}/video.aac".format(input_video, output_audio),
                shell=True,
                check=True)

    subprocess.run("ffmpeg -i {} {}/%05d_video.jpg -hide_banner".format(input_video, output_images),
                shell=True,
                check=True)


if __name__ == '__main__':
    componentExecutor(slice_video).execute(sys.argv)
