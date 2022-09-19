#This program is because I didn't want to Google Circumferences all the time while modeling
#There will be three options, do you want Circumference, radius, and diameter
#You will have the choice of reference, solve off Circumference, radius, or diameter for the counter measurement.

Write-Host "Are you wanting to measure Circumference, Radius, or Repetition?"
Write-Host "1. Circumference"
Write-Host "2. Radius"
#Write-Host "3. Repetition"
$Source = Read-Host "Selection" 

if ($Source -eq 1) 

{
    Write-Host "Calculating the Circumference of the circle"
    $Source = "Circumference"
}

elseif ($Source -eq 2)
{
    Write-Host "Calculating the Radius of the circle"
    $Source = "Radius"
}
else 
{
    Write-Host "Generating repetitive radi"
    $Source = "Frequency"
}

switch ($Source) 

{
    
    Circumference 
    
    {
        Write-Host "What is the dimension of the Radius in cm?"
        $Dimension = Read-Host "Selection"
        $Reference = "Radius"                                    
    }
                  
    Radius 
    
    {
        Write-Host "What is the dimension of the Circumference in cm?"
        $Dimension = Read-Host "Selection"
        $Reference = "Circumference" 
    }

    Frequency
    {
        Write-Host "What distance do you want between circles?"
        $Dimension = Read-Host "Selection"
        $Reference = "Frequency"
    }
}

If ($Reference -eq "Frequency")
{
    Write-Host "How many circles do you want?"
    $Repetitions = Read-Host "Selection"

}
else
{
    Write-Host "Calculating $source using $Reference with measurement of $Dimension"
}


switch ($Source) 
 
{
    Circumference 
    
    {   
        
        $Circumference = [math]::PI * [math]::Pow($Dimension, 2)
        $Circumference_Rounded = [math]::Round($Circumference, 2)
        write-Host "$Circumference_Rounded"    
    }
        
    
    Radius 
    
    {
        $Radius = $Dimension / [math]::PI / 2
        $Radius_Rounded = [math]::Round($Radius, 2)
        write-Host "$Radius_Rounded" 
    
    }

    Frequency
    
    {
        While ($Iterations -lt $Repetitions){
        $Radius = ($Dimension+$Iterations*$Dimension) / [math]::PI / 2  
        $Radius_Rounded = [math]::Round($Radius, 2)
        write-Host "$Radius_Rounded" 
        $Iterations++
        }
    }
    
    }
     $Iterations = $null