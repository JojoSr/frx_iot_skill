import QtQuick 2.0

Item {
    width: 1920
    height: 1080

    Image {
        id: image
        x: 0
        y: 0
        width: 1920
        height: 1080
        source: "net_img.png"
        sourceSize.width: 546
        fillMode: Image.Stretch

        Text {
            id: text1
            x: 140
            y: 116
            color: "#fdfdfd"
            text: qsTr("Synoki Mission Control")
            font.pixelSize: 100
            lineHeightMode: Text.ProportionalHeight
            minimumPointSize: 79
            minimumPixelSize: 80
            fontSizeMode: Text.FixedSize
            textFormat: Text.RichText
        }

        Video{

        }
    }

}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.5}
}
##^##*/
