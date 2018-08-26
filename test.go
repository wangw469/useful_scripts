package main

import "fmt"
import "net/http"
import "os"
// import "io/ioutil"

func main() {
    resp, err := http.Get(fmt.Sprintf("http://%s:%d/", "1.1.1.1", 10080))
    if err != nil {
        fmt.Printf("%s\n", err)
        os.Exit(1)
    }
    fmt.Printf("resp = %d\n", resp.StatusCode)
}
