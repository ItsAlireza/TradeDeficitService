from pydantic import BaseModel, Field


class InferenceSerializer(BaseModel):
    year: int
    covid_dummy: int
    gdp_canada: float = Field(..., alias='GDP of canada, in billions USD')
    gdp_us: float = Field(..., alias='GDP of the US, in billions')
    nominal_exchange_rate: float = Field(..., alias='nominal exchange rate USD/CAD')
    deflator_canada: float
    deflator_usa: float
    cpi_canada: float
    cpi_usa: float
    real_exchange_rate: float = Field(..., alias='real exchange rate using CPI')
    unemployment_rate_us: float = Field(..., alias='unemployment rate US')
    global_econ_policy_uncertainty: float = Field(..., alias='Global econ policy uncertainty index')
    us_econ_policy_uncertainty: float = Field(..., alias='US econ policy uncertainty index')
    m2_us: float = Field(..., alias='M2 US')
    m2_canada: int = Field(..., alias='M2 Canada')
    interest_rate_canada: float = Field(..., alias='interest rate Canada')
    ppi_canada: float = Field(..., alias='PPI Canada')
    ppi_us: float = Field(..., alias='PPI US')
    interest_rate_us: float = Field(..., alias='interest rate US')
    fdi_us: int = Field(..., alias='FDI US')
    migration_fear_us: float = Field(..., alias='migration fear US')

    class Config:
        allow_population_by_field_name = True
