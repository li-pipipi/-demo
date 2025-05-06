import cv2

image_path = "./saved_image.jpg"
image = cv2.imread(image_path)
#检查图像是否成功读取
if image is None:
    print("Error: Could not read the image.")
    exit()

#显示图像
#创建一个名为“Display Image”的窗口，并在其中显示图像
cv2.imshow("My Image", image)
# 等待用户按键
#参数0表示等待无限长的时间，直到用户按下任意键
key = cv2.waitKey(0)
#根据用户按键执行操作
if key == ord('s'): #按下s键保存图像
    output_path = 'saved_image.png'
    cv2.imwrite(output_path, image)
    print(f"图像已保存为{output_path}")
elif key == ord('q'): #按下q键退出程序
    print("程序已退出")
else: #按下其他键退出程序
    print("图像未保存")

#关闭显示窗口
cv2.destroyAllWindows()
#
