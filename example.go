package main

import (
	"fmt"
	"log"
	"encoding/json"
	"github.com/gedex/bp3d"
)

type JItem struct {
	Name string `json:"name"`
	X float64 `json:"x"`
	Y float64 `json:"y"`
	Z float64 `json:"z"`
	Width float64 `json:"width"`
	Length float64 `json:"length"`
	Height float64 `json:"height"`
}

type JBin struct {
	Weight float64 `json:"weight"`
	Width float64 `json:"width"`
	Length float64 `json:"length"`
	Height float64 `json:"height"`
	Volume float64 `json:"volume"`
	Placement []*JItem `json:"placement"`
}

func main() {
	p := bp3d.NewPacker()

	// check weight
	// cannot rotate
	
	// Add bins.
	p.AddBin(bp3d.NewBin("small-envelope", 11.5, 6.125, 0.25, 10))
	p.AddBin(bp3d.NewBin("large-envelope", 15.0, 12.0, 0.75, 15))
	p.AddBin(bp3d.NewBin("small-box", 8.625, 5.375, 1.625, 70.0))
	p.AddBin(bp3d.NewBin("medium-box", 11.0, 8.5, 5.5, 70.0))
	p.AddBin(bp3d.NewBin("medium-2-box", 13.625, 11.875, 3.375, 70.0))
	p.AddBin(bp3d.NewBin("large-box", 12.0, 12.0, 5.5, 70.0))
	p.AddBin(bp3d.NewBin("large-2-box", 23.6875, 11.75, 3.0, 70.0))

	// Add items.
	p.AddItem(bp3d.NewItem("50g [powder 1]", 3.9370, 1.9685, 1.9685, 1))
	p.AddItem(bp3d.NewItem("50g [powder 2]", 3.9370, 1.9685, 1.9685, 2))
	p.AddItem(bp3d.NewItem("50g [powder 3]", 3.9370, 1.9685, 1.9685, 3))
	p.AddItem(bp3d.NewItem("250g [powder 4]", 7.8740, 3.9370, 1.9685, 4))
	p.AddItem(bp3d.NewItem("250g [powder 5]", 7.8740, 3.9370, 1.9685, 5))
	p.AddItem(bp3d.NewItem("250g [powder 6]", 7.8740, 3.9370, 1.9685, 6))
	p.AddItem(bp3d.NewItem("250g [powder 7]", 7.8740, 3.9370, 1.9685, 7))
	p.AddItem(bp3d.NewItem("250g [powder 8]", 7.8740, 3.9370, 1.9685, 8))
	p.AddItem(bp3d.NewItem("250g [powder 9]", 7.8740, 3.9370, 1.9685, 9))

	// Pack items to bins.
	if err := p.Pack(); err != nil {
		log.Fatal(err)
	}

	displayPackedJson(p.Bins)
}

func displayPacked(bins []*bp3d.Bin) {
	for _, b := range bins {
		fmt.Println(b)
		fmt.Println(" packed items:")
		for _, i := range b.Items {
			fmt.Println("  ", i)
		}
	}
}

func displayPackedJson(bins []*bp3d.Bin) {
	for _, b := range bins {
		fmt.Println(b)
		fmt.Println(" packed items:")
		var placement []*JItem
		for _, i := range b.Items {
			fmt.Println("  ", i)
			jitem := &JItem {
				Name: i.Name,
				X: i.Position[0],
				Y: i.Position[1],
				Z: i.Position[2],
				Width: i.GetDimension()[0],
				Height: i.GetDimension()[1],
				Length: i.GetDimension()[2],
			}
			placement = append(placement, jitem)
		}

		jbin := &JBin {
			Weight: b.MaxWeight,
			Width: b.Width,
			Height: b.Height,
			Length: b.Depth,
			Volume: b.Width * b.Depth * b.Height,
			Placement: placement,
		}

		encjson, _ := json.Marshal(jbin)
		fmt.Println(string(encjson))
		fmt.Println()
		fmt.Println()
	}
}