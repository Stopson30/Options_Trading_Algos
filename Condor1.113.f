let ironCondorStrategy underlyingPrice lowerStrikePut upperStrikePut lowerStrikeCall upperStrikeCall timeToExpiration riskFreeRate volatility =
    let lowerPutOption = {
        UnderlyingPrice = underlyingPrice
        StrikePrice = lowerStrikePut
        TimeToExpiration = timeToExpiration
        RiskFreeRate = riskFreeRate
        Volatility = volatility
        OptionType = "put"
    }
    let upperPutOption = {
        UnderlyingPrice = underlyingPrice
        StrikePrice = upperStrikePut
        TimeToExpiration = timeToExpiration
        RiskFreeRate = riskFreeRate
        Volatility = volatility
        OptionType = "put"
    }
    let lowerCallOption =UnderlyingPrice = underlyingPrice
        StrikePrice = lowerStrikeCall
        TimeToExpiration = timeToExpiration
        RiskFreeRate = riskFreeRate
        Volatility = volatility
        OptionType = "call"
    }
    let upperCallOption = {
        UnderlyingPrice = underlyingPrice
        StrikePrice = upperStrikeCall
        TimeToExpiration = timeToExpiration
        RiskFreeRate = riskFreeRate
        Volatility = volatility
        OptionType = "call"
    }

    let lowerPutPremium = blackScholes lowerPutOption
    let upperPutPremium = blackScholes upperPutOption
    let lowerCallPremium = blackScholes lowerCallOption
    let upperCallPremium = blackScholes upperCallOption

    let putSpreadPremium = lowerPutPremium - upperPutPremium
    let callSpreadPremium = lowerCallPremium - upperCallPremium

    putSpreadPremium + callSpreadPremium
