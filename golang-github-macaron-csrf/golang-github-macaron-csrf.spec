%global goipath         github.com/go-macaron/csrf
%global commit          503617c6b37257a55dff6293ec28556506c3a9a8
%global scm             git

%gometa

%global common_description %{expand:
Middleware csrf generates and validates CSRF tokens for Macaron
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                0
Release:                1%{?dist}
Summary:                Middleware csrf generates and validates CSRF tokens for Macaron

License:                Apache-2.0
URL:                    %{gourl}
Source0:                %{gosource}


%description
%{common_description}

%gopkg


%prep
%goprep


%install
%gopkginstall


%files
%gopkgfiles



%changelog
* Mon Nov  4 2019 ElXreno <elxreno@gmail.com>
- Initial packaging
